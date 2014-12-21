# 2014.12.19 21:47:00 CST
from django import forms
from ansible_modules.models import AnsibleModule, AnsibleModuleOption

class AnsibleModuleForm(forms.ModelForm):
   
    class Meta:
        model = AnsibleModule
        exclude = ['created', 'updated']

class AnsibleModuleOptionForm(forms.ModelForm):

    class Meta:
        model = AnsibleModuleOption
        fields = ['module', 'name', 'default', 'required', 'description', 'choices', 'aliases']
