

from django.contrib import admin



from .models import Categoria, Servicio

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria', 'numero_productos', 'categoria_popular')
    list_filter = ('nombre_categoria', 'numero_productos')
    search_fields = ('nombre_categoria',)

admin.site.register(Categoria, CategoriaAdmin)


class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio','categoria','duracion')
    list_filter = ('categoria','precio','duracion', 'numero_reservas')
    search_fields = ('nombre','categoria','descripcion')

admin.site.register(Servicio, ServicioAdmin)
