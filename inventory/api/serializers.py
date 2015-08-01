from rest_framework import serializers
from rest_framework.utils import model_meta
from inventory.models import (
    Inventory, 
    HostGroup, 
    Host
)
import logging
logger = logging.getLogger('django')

class HostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Host
        fields = ('hostname', 'ipaddress', 'port')
        required_fields = ('ipaddress',)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class HostGroupSerializer(serializers.ModelSerializer):
    hosts = HostSerializer(many=True, required=False, read_only=False)

    class Meta:
        model = HostGroup
        fields = ('name', 'hosts')
        required_fields = ('name',)

class InventorySerializer(serializers.ModelSerializer):
    host_groups = HostGroupSerializer(many=True, required=False)
    
    class Meta:
        model = Inventory
        fields = ('name', 'host_groups')
        required_fields = ('name',)

