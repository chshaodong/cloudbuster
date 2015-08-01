from rest_framework import viewsets
from rest_framework.response import Response
from inventory.models import (
    Inventory, 
    HostGroup,
    Host,
)
from inventory.api.serializers import (
    InventorySerializer,
    HostSerializer, 
    HostGroupSerializer,
)


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

    def list(self, request, host_group_pk=None):
        queryset = HostGroup.objects.get(pk=host_group_pk).hosts.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, host_group_pk=None):
        queryset = self.queryset.get(pk=pk, host_group=host_group_pk)
        serializer = self.serializer(queryset)
        return Response(serializer.data)


class HostGroupViewSet(viewsets.ModelViewSet):
    queryset = HostGroup.objects.all()
    serializer_class = HostGroupSerializer
    
    def list(self, request, inventory_pk=None):
        queryset = self.queryset.filter(inventory=inventory_pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, inventory_pk=None, pk=None):
        queryset = self.queryset.get(pk=pk, inventory=inventory_pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

