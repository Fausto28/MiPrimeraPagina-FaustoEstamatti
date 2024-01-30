from django.urls import path

from . import views

app_name= "producto"

urlpatterns = [
    path("", views.index, name="index"),
    #path('productocategoria/list/',views.productocategoria_list ,name='productoscategoria_list'),
    path("productocategoria/list/", views.Productocategorialist.as_view(), name="productocategoria_list"),
    path("productocategoria/create/", views.ProductoCreate.as_view(), name="productocategoria_create")
]