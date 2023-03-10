from django.db import models



class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    descripcion = models.TextField()

    numero_productos = models.PositiveIntegerField(default=0)
    categoria_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_categoria

    class Meta:
        ordering = ['nombre_categoria']

    def aumentar_productos(self):
        self.numero_productos += 1
        self.save()

    def marcar_como_popular(self):
        categorias = Categoria.objects.all()
        for categoria in categorias:
            categoria.categoria_popular = False
            categoria.save()
        self.categoria_popular = True
        self.save()

    def obtener_categorias_populares(self):
        categorias_populares = Categoria.objects.filter(categoria_popular=True)
        return categorias_populares



class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    numero_visitas = models.PositiveIntegerField(default=0)
    duracion_lectura_promedio = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-numero_visitas']

    def aumentar_visitas(self):
        self.numero_visitas += 1

    def calcular_duracion_lectura_promedio(self):
        tiempo_estimado_lectura = 2 # en minutos
        num_palabras = len(self.descripcion.split())
        duracion = num_palabras * tiempo_estimado_lectura
        self.duracion_lectura_promedio = duracion
        self.save()

    def obtener_articulos_similares(self):
        articulos_similares = Articulo.objects.filter(categoria=self.categoria).exclude(id=self.id)
        articulos_similares = articulos_similares.order_by('-numero_visitas')[:5]
        return articulos_similares

