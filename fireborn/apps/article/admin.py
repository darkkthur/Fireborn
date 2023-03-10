from django.contrib import admin



from .models import Categoria, Articulo

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria', 'numero_productos', 'categoria_popular')
    list_filter = ('nombre_categoria', 'numero_productos')
    search_fields = ('nombre_categoria',)

admin.site.register(Categoria, CategoriaAdmin)



class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor','fecha_publicacion','categoria','numero_visitas','duracion_lectura_promedio')
    list_filter = ('autor', 'fecha_publicacion','categoria','duracion_lectura_promedio')
    search_fields = ('titulo','autor','descripcion','categoria')

admin.site.register(Articulo, ArticuloAdmin)
