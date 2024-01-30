from django.urls import path

from . import views

app_name= "producto"

urlpatterns = [
    path("", views.index, name="index"),
    #path('productocategoria/list/',views.productocategoria_list ,name='productoscategoria_list'),
    path("producto/list/", views.Productolist.as_view(), name="producto_list"),
    path("producto/create/", views.ProductoCreate.as_view(), name="producto_create")
]