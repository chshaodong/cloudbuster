from django import forms
from ansible_modules.models import AnsibleModule

class AnsibleModuleForm(forms.ModelForm):
    class Meta:
        model = AnsibleModule
        exclude = ['created', 'updated']
