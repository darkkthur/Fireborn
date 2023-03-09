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

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=100)
    cuerpo = models.TextField()

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    numero_visitas = models.PositiveIntegerField(default=0)
    destacada = models.BooleanField(default=False)
    duracion_lectura_promedio = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_publicacion']

    def aumentar_visitas(self):
        self.numero_visitas += 1
        self.save()

    def calcular_tiempo_desde_publicacion(self):
        from django.utils import timezone
        tiempo_pasado = timezone.now() - self.fecha_publicacion
        return tiempo_pasado.total_seconds() // 60

    def obtener_palabras_clave(self):
        from collections import Counter
        from string import punctuation
        palabras = self.cuerpo.lower().split()
        palabras = [p.strip(punctuation) for p in palabras]
        palabras = [p for p in palabras if len(p) > 3]
        palabras_comunes = ['a', 'ante', 'bajo', 'con', 'de', 'desde', 'en', 'entre', 'hacia', 'hasta', 'para', 'por', 'según', 'sin', 'sobre', 'tras', 'y']
        palabras = [p for p in palabras if p not in palabras_comunes]
        contador = Counter(palabras)
        palabras_clave = contador.most_common(5)
        return palabras_clave

    def calcular_duracion_lectura_promedio(self):
        tiempo_estimado_lectura = 2 # en minutos
        num_palabras = len(self.descripcion.split())
        duracion = num_palabras * tiempo_estimado_lectura
        self.duracion_lectura_promedio = duracion
        self.save()

    def obtener_noticias_similares(self):
        articulos_similares = Noticia.objects.filter(categoria=self.categoria).exclude(id=self.id)
        articulos_similares = articulos_similares.order_by('-numero_visitas')[:5]
        return articulos_similares

