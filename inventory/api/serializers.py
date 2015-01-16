from rest_framework import serializers
from inventory.models import (
    Inventory, 
    InventoryVar,
    HostGroup, 
    HostGroupVar,
    Host,
    HostVar
)


class BaseVarSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        for key, value in data.iteritems():
            return {'key': key, 'value': value}

    def to_representation(self, obj):
        return { obj.key: obj.value }


class HostVarSerializer(BaseVarSerializer):
    class Meta:
        model = HostVar
        fields = ('key', 'value')
        required_fields = ('key',)

class HostSerializer(serializers.ModelSerializer):
    vars = HostVarSerializer(many=True)
    class Meta:
        model = Host
        fields = ('name', 'vars', 'port')
        required_fields = ('name',)

    def create(self, validated_data):
        vars_data = validated_data.pop('vars')
        host = Host.objects.create(**validated_data)
        for var in vars_data:
            host.add_var(**var)
        host.save()
        return host


class HostGroupVarSerializer(BaseVarSerializer):
    class Meta:
        model = HostGroupVar
        fields = ('key', 'value')
        required_fields = ('key',)

class HostGroupSerializer(serializers.ModelSerializer):
    hosts = HostSerializer(many=True, required=False)
    vars = HostGroupVarSerializer(many=True)
    class Meta:
        model = HostGroup
        fields = ('name', 'vars', 'hosts')
        required_fields = ('name')

    def create(self, validated_data):
        vars_data = validated_data.pop('vars')
        hosts_data = validated_data.pop('hosts')
        host_group = HostGroup.objects.create(**validated_data)
        for var in vars_data:
            host_group.add_var(**var)
        for host in hosts_data:
            host_group.add_host(**host)
        host_group.save()
        return host_group


class InventoryVarSerializer(BaseVarSerializer):
    class Meta:
        model = InventoryVar
        fields = ('key', 'value')
        required_fields = ('key',)

class InventorySerializer(serializers.ModelSerializer):
    host_groups = HostGroupSerializer(many=True, required=False)
    vars = InventoryVarSerializer(many=True, required=False)
    
    class Meta:
        model = Inventory
        fields = ('name', 'vars', 'host_groups')
        required_fields = ('name',)

    def create(self, validated_data):
        vars_data = validated_data.pop('vars')
        host_group_data = validated_data.pop('host_groups')
        inventory = Inventory.objects.create(**validated_data)
        for var in vars_data: 
            if var is not None:
                inventory.add_var(**var)
        for host_group in host_group_data:
            host_group_vars = host_group.pop('vars')
            hosts = host_group.pop('hosts')
            hostgroup = inventory.add_host_group(**host_group)
            for var in host_group_vars: 
                if var is not None:
                    hostgroup.add_var(**var)
            for host_data in hosts:
                vars = host_data.pop('vars')
                host = hostgroup.add_host(**host_data)
                for var in vars: 
                    if var is not None:
                        host.add_var(**var)
                host.save()
            hostgroup.save()
        inventory.save()
        return inventory


