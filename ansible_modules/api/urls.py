from django.conf.urls import patterns, include, url
from rest_framework_nested import routers
from ansible_modules.api.views import (
    ModuleCategoryViewSet
)

router = routers.SimpleRouter()
router.register(r'modules', ModuleCategoryViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
