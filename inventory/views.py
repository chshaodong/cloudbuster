from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView
from inventory.models import Inventory, HostGroup, Host

class InventoryListView(ListView):
    queryset = Inventory.objects.all()
    model = Inventory
    context_object_name = 'inventories'
    
class InventoryDetailView(DetailView):
    model = Inventory
    
    def get_context_data(self, **kwargs):
        context = super(InventoryDetailView, self).get_context_data(**kwargs)
        context['hostgroups'] = context['inventory'].get_groups()
        return context

   
