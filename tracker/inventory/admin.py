from django.contrib import admin
import inventory.models
# Register your models here.

admin.site.register(inventory.models.Shipment)
admin.site.register(inventory.models.Pallet)
admin.site.register(inventory.models.Device)
admin.site.register(inventory.models.UserProfile)
admin.site.register(inventory.models.Donor)
admin.site.register(inventory.models.DevLogEntry)
admin.site.register(inventory.models.ActionPoint)
