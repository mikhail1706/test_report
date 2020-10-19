from django.contrib import admin
from .models import InputFiles, CfnInventory, InventoryListing, ReservedInventory, GeneratedReport, Asin

# Register your models here.
admin.site.register(GeneratedReport)
admin.site.register(InputFiles)
admin.site.register(CfnInventory)
admin.site.register(InventoryListing)
admin.site.register(ReservedInventory)
admin.site.register(Asin)