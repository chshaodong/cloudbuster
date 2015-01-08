from django.test import TestCase
from inventory.models import Inventory, HostGroup, Host

class TestCloudBusterInventory(TestCase):

    def test_host_vars(self):
        inventory = Inventory.objects.create(name='default')
        host = Host.objects.create(inventory=inventory, name='192.168.33.10')

        vars = {'a': True, 'b': False, 'foo': 'bar'}
        for k, v in vars.iteritems():
            host.set_variable(k, v)
        
        host_vars = host.get_variables()
        self.assertTrue(host_vars == vars)

    def test_hostgroup_vars(self):
        inventory = Inventory.objects.create(name='default')
        hostgroup = HostGroup.objects.create(inventory=inventory, name='test')
    
        vars = {'a': True, 'b': False, 'foo': 'bar'}
        for k, v in vars.iteritems():
            hostgroup.set_variable(k, v)

        hostgroup_vars = hostgroup.get_variables()
        self.assertTrue(hostgroup_vars == vars)

    def test_hostgroup_add_get_hosts(self):
        inventory = Inventory.objects.create(name='default')
        webservers = HostGroup.objects.create(inventory=inventory, name='webservers')
        webserver0 = Host.objects.create(inventory=inventory, name='www0.example.com')
        
        webservers.add_host(webserver0)
        self.assertTrue(webservers.get_hosts()[0].name == webserver0.name)
        
    def test_hostgroup_add_get_child_groups(self):
        inventory = Inventory.objects.create(name='default')
        parent = HostGroup.objects.create(inventory=inventory, name='webservers')
        child = HostGroup.objects.create(inventory=inventory, name='webservers_children')

        parent.add_child_group(child)
        self.assertTrue(parent.children.all()[0].name == child.name)


