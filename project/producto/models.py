from django.db import models
from django.utils import timezone
# Create your models here.

class ProductoCategoria (models.Model):
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True, verbose_name='descripción')
    
    def __str__(self) -> str:
        return self.categoria
    
class Producto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    precio = models.FloatField()
    unidad_medida = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True, verbose_name='descripción')
    fecha_actualizacion=models.DateField(null=True, blank=True, default=timezone.now,editable=False, verbose_name='Fecha de actualización')
    categoria_id = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f"{self.marca}, {self.modelo} {self.unidad_medida} ${self.precio}"
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"