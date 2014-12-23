from django.test import TestCase
from django.test.client import RequestFactory
from ansible_modules.views import AnsibleModuleListView
from django.core.management import call_command

class AnsibleModuleListViewTests(TestCase):
    """Ansible modules view tests.."""

    def setUp(self):
        call_command('load_ansible_modules')        
    
    def test_build_module_categories(self):
        call_command('build_module_categories')

    def _test_module_list_view(self):
        '''
        Verifies that list view returns modules and related options.
        '''

        #make a request to get the modules list view.
        factory = RequestFactory()
        request = factory.get('/ansible/modules/')

        # get the response object        
        response = AnsibleModuleListView.as_view()(request)

        # iterate through object_list, printing the module path
        for module in response.context_data['object_list']:
            # for all related options
            for option in module.options.all():
                self.assertTrue(option.required in ['yes','no'])

    def _test_by_category(self):
        factory = RequestFactory()
        
        for module_path in ['/extras/web_infrastructure/jira']:
            request = factory.get('/ansible/modules/%s/' % module_path)
            response = AnsibleModuleListView.as_view()(request, module_path)
                        


