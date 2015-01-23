from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase

from inventory.models import (
    Inventory,
    InventoryVar,
    HostGroup,
    HostGroupVar,
    Host,
    HostVar
)

class TestCloudBusterInventoryAPI(APITestCase):

    def __init__(self, *args, **kwargs):
        super(TestCloudBusterInventoryAPI, self).__init__(*args, **kwargs)
        self.maxDiff = None

    def test_00create_inventory(self):
        data = {
            "name": "dev",
            "vars": [],
            "host_groups": []
        }
        url = r'/api/inventories/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(dict(response.data), data)

    def test_01create_inventory_with_vars(self):
        data = {
            "name": "dev",
            "vars": [{"inventory_test_var": "test_value"}],
            "host_groups": []
        }       
        url = r'/api/inventories/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(dict(response.data), data)

    def test_02create_inventory_with_hostgroups_and_hostgroup_vars(self):
        data = {
            "name": "dev",
            "vars": [{"inventory_test_var": "test_value"}],
            "host_groups": [{
                "name": "webservers", 
                "vars": [{
                        "host_group_test_var": "Host_group_test_value"
                        }], 
                "hosts": []
            }] 
        }       
        url = r'/api/inventories/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(dict(response.data), data)

    def test_03create_inventory_with_hostgroups_and_hostgroup_vars_and_hosts(self):
        data = { "name": "Prod", 
    "vars": [
        {
            "test": "test_data"
        }, 
        {
            "test1": "test_data1"
        }
    ], 
    "host_groups": [
        {
            "name": "webservers", 
            "vars": [
                {
                    "test": "testing"
                }
            ], 
            "hosts": [
                {
                    "name": "www0.example.com", 
                    "vars": [],
                    "port": None
                }, 
                {
                    "name": "www1.example.com", 
                    "vars": [],
                    "port": 2222
                }]
        }]
    }

        url = r'/api/inventories/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(dict(response.data), data)
