from django.contrib import admin
from inventory.models import (
    Inventory, InventoryVar,
    HostGroup, HostGroupVar,
    Host, HostVar
)

admin.site.register(HostGroup)
admin.site.register(HostGroupVar)
admin.site.register(Host)
admin.site.register(HostVar)
admin.site.register(Inventory)
admin.site.register(InventoryVar)
