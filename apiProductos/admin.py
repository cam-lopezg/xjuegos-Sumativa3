from django.contrib import admin
from .models import Carrito, Producto, AuxCarritoProducto
# Register your models here.

admin.site.register(Carrito)
admin.site.register(Producto)
admin.site.register(AuxCarritoProducto)