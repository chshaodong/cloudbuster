from django.conf.urls import patterns, include, url
from rest_framework_nested import routers
from inventory.api.views import (
    HostViewSet, 
    HostGroupViewSet,
    InventoryViewSet
)

router = routers.SimpleRouter()
router.register(r'inventories', InventoryViewSet)
inventory_router = routers.NestedSimpleRouter(router, r'inventories', lookup='inventory')
inventory_router.register(r'host_groups', HostGroupViewSet)
host_group_router = routers.NestedSimpleRouter(inventory_router, r'host_groups', lookup='host_group')
host_group_router.register(r'hosts', HostViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^', include(inventory_router.urls)),
    url(r'^', include(host_group_router.urls)),
)
