from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria', 'numero_productos', 'categoria_popular')
    list_filter = ('nombre_categoria', 'numero_productos')
    search_fields = ('nombre_categoria',)

admin.site.register(Categoria, CategoriaAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion','categoria','precio','cantidad_inventario','numero_ventas')
    list_filter = ( 'numero_ventas','categoria','destacado','cantidad_inventario')
    search_fields = ('nombre','categoria','descripcion')

admin.site.register(Producto, ProductoAdmin)
