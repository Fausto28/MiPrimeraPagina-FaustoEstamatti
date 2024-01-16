from django.contrib import admin

from .models import Cliente, Pais, Auto

# Register your models here.


admin.site.register(Pais)
admin.site.register(Cliente)
admin.site.register(Auto)
