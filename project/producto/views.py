from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import ProductoCategoria
# Create your views here.

def index(request):
    return render(request, "producto/index.html")

'''
def productocategoria_list(request):
    objects = ProductoCategoria.objects.all()
    context= {'objects_list': objects}
    return render(request, "producto/productocategoria_list.html", context)
'''

class Productocategorialist(ListView):
    model = ProductoCategoria
    
    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get('consulta'):
            consultar=self.request.GET.get('consulta')
            object_list=ProductoCategoria.objects.filter(categoria__icontains=consultar)    
        else: 
            object_list=ProductoCategoria.objects.all()
        return object_list