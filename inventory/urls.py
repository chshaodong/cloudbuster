from django.conf.urls import patterns, include, url
from inventory.views import InventoryListView, InventoryDetailView

urlpatterns = patterns('',
        url(r'^inventory/$', InventoryListView.as_view(), name='inventory_listview'),
        url(r'^inventory/(?P<pk>.+)/', InventoryDetailView.as_view(), name='inventory_detailview'),
)

