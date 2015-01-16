from rest_framework import viewsets
from inventory.models import (
    Inventory, 
    InventoryVar,
    HostGroup,
    HostGroupVar,
    Host,
    HostVar
)
from inventory.api.serializers import (
    InventorySerializer,
    InventoryVarSerializer,
    HostSerializer, 
    HostVarSerializer,
    HostGroupSerializer,
    HostGroupVarSerializer,
)


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class HostVarViewSet(viewsets.ModelViewSet):
    queryset = HostVar.objects.all()
    serializer_class = HostVarSerializer


class HostGroupViewSet(viewsets.ModelViewSet):
    queryset = HostGroup.objects.all()
    serializer_class = HostGroupSerializer

class HostGroupVarViewSet(viewsets.ModelViewSet):
    queryset = HostGroupVar.objects.all()
    serializer_class = HostGroupVarSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryVarViewSet(viewsets.ModelViewSet):
    queryset = InventoryVar.objects.all()
    serializer_class = InventoryVarSerializer

