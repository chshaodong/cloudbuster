from rest_framework import serializers
from rest_framework.utils import model_meta
from ansible_modules.models import (ModuleCategory,
                                    AnsibleModule,
                                    AnsibleModuleOption)

import logging
logger = logging.getLogger('django')

class AnsibleModuleOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnsibleModuleOption
        fields = ('name', 'default', 'required', 'description', 'choices', 'aliases')

class AnsibleModuleSerializer(serializers.ModelSerializer):
    options = AnsibleModuleOptionSerializer(many=True)
    
    class Meta:
        model = AnsibleModule
        fields = ('id', 'description', 'name', 
                  'option_keys', 'docuri',
                  'requirements', 'author',
                  'filename', 'version_added',
                  'short_description', 'module_path', 
                  'created', 'updated', 'options')

#AnsibleModuleSerializer.base_fields['options'] = AnsibleModuleOptionSerializer(many=True)

class ModuleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleCategory
        fields = ('id', 'parent', 'name', 'slug', 'subcategories', 'modules')


