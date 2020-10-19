import logging

import pandas
from pandas import ExcelWriter
from reportTestProject.celery import app
import time

from django.conf import settings

from .models import InputFiles
from .utils import save_cfn_inventory_report, save_inventory_listing_report, \
    save_reserved_inventory_report, save_generated_report

info_logger = logging.getLogger('info_logger')
error_logger = logging.getLogger('error_logger')


@app.task(name='upload_reports', queue='reports')
def upload_reports(input_files_id: int):
    result = {'success'}

    try:
        input_files = InputFiles.objects.get(id=input_files_id)
    except InputFiles.DoesNotExist:
        result['success'] = False
        error_logger.error(f'InputFiles does not exit. Id: {input_files_id}')
        return result

    save_cfn_inventory_report(input_files.cfn_inventory.path)

    save_inventory_listing_report(input_files.inventory_listing.path)

    save_reserved_inventory_report(input_files.reserved_inventory.path)

    return {'msg': 'success'}


@app.task(name='generate_data', queue='reports')
def generate_data(input_files_id):
    result = {}
    try:
        input_files = InputFiles.objects.get(id=input_files_id)
    except InputFiles.DoesNotExist:
        error_logger.error(f'InputFiles does not exit. Hash: {input_files_id}')
        return

    cfn_inventory = pandas.read_csv(input_files.cfn_inventory)
    inventory_listing = pandas.read_csv(input_files.inventory_listing)
    reserved_inventory = pandas.read_csv(input_files.reserved_inventory)

    cfn_inventory = cfn_inventory.loc[cfn_inventory['condition'] == 'New']
    inventory_listing = inventory_listing.loc[inventory_listing['condition'] == 'New']

    cfn_grouped = cfn_inventory.groupby('asin').agg({
        'sku': 'first', 'product-name': 'first', 'condition': 'first', 'your-price': 'first',
        'cfn-warehouse-quantity': 'sum', 'cfn-fulfillable-quantity': 'sum', 'cfn-unsellable-quantity': 'sum',
        'cfn-reserved-quantity': 'sum', 'cfn-total-quantity': 'sum'})

    inventory_grouped = inventory_listing.groupby('asin').agg({
        'sku': 'first', 'fnsku': 'first', 'product-name': 'first', 'condition': 'first', 'your-price': 'first',
        'mfn-listing-exists': 'first', 'mfn-fulfillable-quantity': 'sum', 'afn-listing-exists': 'first',
        'afn-warehouse-quantity': 'sum', 'afn-fulfillable-quantity': 'sum', 'afn-unsellable-quantity': 'sum',
        'afn-reserved-quantity': 'sum', 'afn-total-quantity': 'sum', 'per-unit-volume': 'first',
        'afn-inbound-working-quantity': 'sum', 'afn-inbound-shipped-quantity': 'sum',
        'afn-inbound-receiving-quantity': 'sum', 'afn-researching-quantity': 'sum',
        'afn-reserved-future-supply': 'sum', 'afn-future-supply-buyable': 'sum',
    })

    reserved_grouped = reserved_inventory.groupby('asin').agg({
        'sku': 'first',
        'product-name': 'first',
        'reserved_qty': 'sum',
        'reserved_customerorders': 'sum',
        'reserved_fc-transfers': 'sum',
        'reserved_fc-processing': 'sum',
    })

    merged = cfn_grouped.merge(inventory_grouped, on=['asin', 'sku', 'product-name', 'condition', 'your-price']) \
        .merge(reserved_grouped, on=['asin', 'sku', 'product-name'])

    current_time = time.strftime("%d.%m.%Y_%H:%M")
    file_path = f'{settings.MEDIA_ROOT}/generated_files/generated_report_{current_time}.xlsx'

    with ExcelWriter(file_path) as file:
        merged.to_excel(file, columns=['sku',
                                       'fnsku',
                                       'product-name',
                                       'condition',
                                       'your-price',
                                       'mfn-listing-exists',
                                       'mfn-fulfillable-quantity',
                                       'afn-listing-exists',
                                       'afn-warehouse-quantity',
                                       'afn-fulfillable-quantity',
                                       'afn-unsellable-quantity',
                                       'afn-reserved-quantity',
                                       'afn-total-quantity',

                                       'per-unit-volume',
                                       'afn-inbound-working-quantity',
                                       'afn-inbound-shipped-quantity',
                                       'afn-inbound-receiving-quantity',
                                       'afn-researching-quantity',
                                       'afn-reserved-future-supply',
                                       'afn-future-supply-buyable',

                                       'reserved_qty',
                                       'reserved_customerorders',
                                       'reserved_fc-transfers',
                                       'reserved_fc-processing',
                                       
                                       'cfn-warehouse-quantity',
                                       'cfn-fulfillable-quantity',
                                       'cfn-unsellable-quantity',
                                       'cfn-reserved-quantity',
                                       'cfn-total-quantity',
                                       ])

    save_generated_report(file_path)
    result['file_path'] = f'{settings.MEDIA_URL}generated_files/generated_report_{current_time}.xlsx'
    return result
