import csv
import json
import logging

from openpyxl import load_workbook

from .models import Sku, Asin, CfnInventory, InventoryListing, ReservedInventory, GeneratedReport


info_logger = logging.getLogger('info_logger')
error_logger = logging.getLogger('error_logger')


def save_cfn_inventory_report(report_file_path):
    with open(report_file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sku, flag = Sku.objects.get_or_create(value=row['sku'])
            asin, flag = Asin.objects.get_or_create(value=row['asin'])

            CfnInventory.objects.create(
                sku=sku,
                asin=asin,
                product_name=row['product-name'],
                condition=row['condition'],
                your_price=row['your-price'],
                cfn_warehouse_quantity=row.get('cfn-warehouse-quantity') or None,
                cfn_fulfillable_quantity=row.get('cfn-fulfillable-quantity') or None,
                cfn_unsellable_quantity=row.get('cfn-unsellable-quantity') or None,
                cfn_reserved_quantity=row.get('cfn-reserved-quantity') or None,
                cfn_total_quantity=row.get('cfn-total-quantity') or None
            )

        info_logger.info('cfn_inventory report has been created')


def save_inventory_listing_report(report_file_path):
    with open(report_file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            sku, flag = Sku.objects.get_or_create(value=row['sku'])
            asin, flag = Asin.objects.get_or_create(value=row['asin'])
            InventoryListing.objects.create(
                sku=sku,
                fnsku=row['fnsku'],
                asin=asin,

                product_name=row['product-name'],
                condition=row['condition'],
                your_price=row.get('your-price') or None,

                mfn_listing_exists=json.loads(row['mfn-listing-exists']),
                mfn_fulfillable_quantity=row.get('mfn-fulfillable-quantity') or None,

                afn_listing_exists=json.loads(row['afn-listing-exists']),
                afn_warehouse_quantity=row['afn-warehouse-quantity'],
                afn_fulfillable_quantity=row['afn-fulfillable-quantity'],
                afn_unsellable_quantity=row['afn-unsellable-quantity'],
                afn_reserved_quantity=row['afn-reserved-quantity'],
                afn_total_quantity=row['afn-total-quantity'],

                per_unit_volume=row.get('per-unit-volume') or None,

                afn_inbound_working_quantity=row['afn-inbound-working-quantity'],
                afn_inbound_shipped_quantity=row['afn-inbound-shipped-quantity'],
                afn_inbound_receiving_quantity=row['afn-inbound-receiving-quantity'],
                afn_researching_quantity=row['afn-researching-quantity'],
                afn_reserved_future_supply=row['afn-reserved-future-supply'],
                afn_future_supply_buyable=row['afn-future-supply-buyable'],
            )
        info_logger.info('inventory_listing report has been created')


def save_reserved_inventory_report(report_file_path):
    with open(report_file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            sku, flag = Sku.objects.get_or_create(value=row['sku'])
            asin, flag = Asin.objects.get_or_create(value=row['asin'])

            ReservedInventory.objects.create(
                sku=sku,
                asin=asin,
                product_name=row['product-name'],
                reserved_qty=row.get('reserved_qty') or None,
                reserved_customer_orders=row.get('reserved_customerorders') or None,
                reserved_fc_transfers=row.get('reserved_fc-transfers') or None,
                reserved_fc_processing=row.get('reserved_fc-processing') or None,
            )
        info_logger.info('reserved_inventory report has been created')


def save_generated_report(report_file_path):
    wb = load_workbook(filename=report_file_path)
    sheet_obj = wb.active
    counter = 0

    for row in sheet_obj.rows:
        if counter == 0:
            counter += 1
            continue

        report = GeneratedReport.objects.create(
            asin=row[0].value,
            sku=row[1].value,
            fnsku=row[2].value,

            product_name=row[3].value,
            condition=row[4].value,
            your_price=row[5].value,

            mfn_listing_exists=bool(row[6].value),
            mfn_fulfillable_quantity=row[7].value,

            afn_listing_exists=bool(row[8].value),
            afn_warehouse_quantity=row[9].value,
            afn_fulfillable_quantity=row[10].value,
            afn_unsellable_quantity=row[11].value,
            afn_reserved_quantity=row[12].value,
            afn_total_quantity=row[13].value,

            per_unit_volume=row[14].value,

            afn_inbound_working_quantity=row[15].value,
            afn_inbound_shipped_quantity=row[16].value,
            afn_inbound_receiving_quantity=row[17].value,
            afn_researching_quantity=row[18].value,
            afn_reserved_future_supply=row[19].value,
            afn_future_supply_buyable=row[20].value,

            reserved_qty=row[21].value,
            reserved_customer_orders=row[22].value,
            reserved_fc_transfers=row[23].value,
            reserved_fc_processing=row[24].value,

            cfn_warehouse_quantity=row[25].value,
            cfn_fulfillable_quantity=row[26].value,
            cfn_unsellable_quantity=row[27].value,
            cfn_reserved_quantity=row[28].value,
            cfn_total_quantity=row[29].value,
        )
