from django.test import TestCase
from django.test.client import RequestFactory
from ansible_modules.views import AnsibleModuleListView
from django.core.management import call_command

class AnsibleModuleListViewTests(TestCase):
    """Ansible modules view tests.."""

    def test_module_import_and_list_view(self):
        '''
        Import Ansible Modules and call a listview.
        Verify that list view returns modules and related options.
        '''

        #make a request to get the modules list view.
        factory = RequestFactory()
        request = factory.get('/ansible/modules/')
        call_command('load_ansible_modules')        

        # get the response object        
        response = AnsibleModuleListView.as_view()(request)

        # iterate through object_list, printing the module path
        for module in response.context_data['object_list']:
            # for all related options
            for option in module.options.all():
                self.assertTrue(option.required in ['yes','no'])

