from django.contrib import admin
from inventory.models import Inventory, HostGroup, Host

admin.site.register(Inventory)
admin.site.register(HostGroup)
admin.site.register(Host)

