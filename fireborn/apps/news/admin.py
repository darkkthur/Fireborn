from django.contrib import admin


from .models import Categoria, Noticia

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria', 'numero_productos', 'categoria_popular')
    list_filter = ('nombre_categoria', 'numero_productos')
    search_fields = ('nombre_categoria',)

admin.site.register(Categoria, CategoriaAdmin)



class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor','fecha_publicacion','categoria','numero_visitas','duracion_lectura_promedio')
    list_filter = ('autor', 'fecha_publicacion','categoria','duracion_lectura_promedio', 'destacada')
    search_fields = ('titulo','autor','cuerpo','categoria')

admin.site.register(Noticia, NoticiaAdmin)
