from rest_framework import viewsets
from rest_framework.response import Response
from ansible_modules.models import (
    ModuleCategory,
    AnsibleModule,
    AnsibleModuleOption
)

from ansible_modules.api.serializers import (
    ModuleCategorySerializer,
    AnsibleModuleSerializer,
    AnsibleModuleOptionSerializer
)

class ModuleCategoryViewSet(viewsets.ModelViewSet):
    queryset = ModuleCategory.objects.all()
    model = ModuleCategory
    serializer_class = ModuleCategorySerializer

#    def serialize_tree(self, queryset):
#        for obj in queryset:
#            data = self.get_serializer(obj).data
#            data['subcategories'] = self.serialize_tree(obj.subcategories.all())
#            yield data
#
#    def list(self, request):
#        queryset = self.get_queryset()
#        data = self.serialize_tree(queryset)
#        return Response(data)
#
#    def retrieve(self, request, pk=None):
#        self.object = self.get_object()
#        data = self.serialize_tree([self.object])
#        return Response(data)


