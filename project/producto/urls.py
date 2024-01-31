from django.urls import path

from . import views

app_name= "producto"

urlpatterns = [
    path("", views.index, name="index"),
    #path('productocategoria/list/',views.productocategoria_list ,name='productoscategoria_list'),
    path("producto/list/", views.Productolist.as_view(), name="producto_list"),
    path("producto/productocategorialist/", views.ProductoCategorialist.as_view(), name="productocategoria_list"),
    path("producto/create/", views.ProductoCreate.as_view(), name="producto_create"),
    path("producto/detail/<int:pk>/", views.ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
    path("producto/update/<int:pk>/", views.ProductoUpdate.as_view(), name="producto_update"),
    path("producto/delete/<int:pk>/", views.ProductoDelete.as_view(), name="producto_delete"),
]