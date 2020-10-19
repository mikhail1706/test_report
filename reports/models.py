from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GeneratedReport(TimeStampedModel):
    asin = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    fnsku = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255, null=True)
    condition = models.CharField(max_length=255, null=True)
    your_price = models.CharField(max_length=255, null=True)
    mfn_listing_exists = models.BooleanField()
    mfn_fulfillable_quantity = models.IntegerField(null=True)
    afn_listing_exists = models.BooleanField()
    afn_warehouse_quantity = models.IntegerField(null=True)
    afn_fulfillable_quantity = models.IntegerField()
    afn_unsellable_quantity = models.IntegerField()
    afn_reserved_quantity = models.IntegerField()
    afn_total_quantity = models.IntegerField()
    per_unit_volume = models.FloatField(null=True)
    afn_inbound_working_quantity = models.IntegerField()
    afn_inbound_shipped_quantity = models.IntegerField()
    afn_inbound_receiving_quantity = models.IntegerField()
    afn_researching_quantity = models.IntegerField()
    afn_reserved_future_supply = models.IntegerField()
    afn_future_supply_buyable = models.IntegerField()

    reserved_qty = models.IntegerField(null=True)
    reserved_customer_orders = models.IntegerField(null=True)
    reserved_fc_transfers = models.IntegerField(null=True)
    reserved_fc_processing = models.IntegerField(null=True)

    cfn_warehouse_quantity = models.IntegerField(null=True)
    cfn_fulfillable_quantity = models.IntegerField(null=True)
    cfn_unsellable_quantity = models.IntegerField(null=True)
    cfn_reserved_quantity = models.IntegerField(null=True)
    cfn_total_quantity = models.IntegerField(null=True)


class InputFiles(TimeStampedModel):
    cfn_inventory = models.FileField(upload_to='input_files/')
    inventory_listing = models.FileField(upload_to='input_files/')
    reserved_inventory = models.FileField(upload_to='input_files/')

    report = models.ForeignKey(GeneratedReport, on_delete=models.CASCADE, null=True)


class Asin(TimeStampedModel):
    value = models.CharField(max_length=255)


class Sku(TimeStampedModel):
    value = models.CharField(max_length=255)


class CfnInventory(TimeStampedModel):
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    asin = models.ForeignKey(Asin, on_delete=models.CASCADE)

    product_name = models.CharField(max_length=255, null=True)
    condition = models.CharField(max_length=255, null=True)
    your_price = models.CharField(max_length=255, null=True)

    cfn_warehouse_quantity = models.IntegerField(null=True)
    cfn_fulfillable_quantity = models.IntegerField(null=True)
    cfn_unsellable_quantity = models.IntegerField(null=True)
    cfn_reserved_quantity = models.IntegerField(null=True)
    cfn_total_quantity = models.IntegerField(null=True)


class InventoryListing(TimeStampedModel):
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    fnsku = models.CharField(max_length=255)
    asin = models.ForeignKey(Asin, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, null=True)
    condition = models.CharField(max_length=255, null=True)

    your_price = models.FloatField(null=True)
    mfn_listing_exists = models.BooleanField()
    mfn_fulfillable_quantity = models.IntegerField(null=True)
    afn_listing_exists = models.BooleanField()
    afn_warehouse_quantity = models.IntegerField(null=True)
    afn_fulfillable_quantity = models.IntegerField()
    afn_unsellable_quantity = models.IntegerField()
    afn_reserved_quantity = models.IntegerField()
    afn_total_quantity = models.IntegerField()
    per_unit_volume = models.FloatField(null=True)
    afn_inbound_working_quantity = models.IntegerField()
    afn_inbound_shipped_quantity = models.IntegerField()
    afn_inbound_receiving_quantity = models.IntegerField()
    afn_researching_quantity = models.IntegerField()
    afn_reserved_future_supply = models.IntegerField()
    afn_future_supply_buyable = models.IntegerField()


class ReservedInventory(TimeStampedModel):
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    asin = models.ForeignKey(Asin, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)

    reserved_qty = models.IntegerField(null=True)
    reserved_customer_orders = models.IntegerField(null=True)
    reserved_fc_transfers = models.IntegerField(null=True)
    reserved_fc_processing = models.IntegerField(null=True)







