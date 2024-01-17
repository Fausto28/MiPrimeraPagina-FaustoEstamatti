from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_title = 'Productos'

class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'descripcion')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','unidad_medida','precio')
    list_display_links=('marca','modelo')
    search_fields=('marca', 'modelo')
    ordering=('categoria_id', 'marca', 'modelo')
    list_filter=('categoria_id','modelo')
    date_hierarchy=('fecha_actualizacion')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(ProductoCategoria, ProductoCategoriaAdmin)