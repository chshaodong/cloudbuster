from rest_framework import routers
from inventory.api.views import (
    HostViewSet, 
    HostVarViewSet,
    HostGroupViewSet,
    HostGroupVarViewSet,
    InventoryViewSet,
    InventoryVarViewSet
)

router = routers.SimpleRouter()
router.register(r'hosts', HostViewSet)
router.register(r'host_vars', HostVarViewSet)
router.register(r'host_groups', HostGroupViewSet)
router.register(r'host_groups_vars', HostGroupVarViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'inventories_vars', InventoryVarViewSet)
urlpatterns = router.urls
