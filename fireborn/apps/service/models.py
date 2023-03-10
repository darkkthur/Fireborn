
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

class Servicio(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.PositiveIntegerField()

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    numero_reservas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['-numero_reservas']

    def aumentar_reservas(self):
        self.numero_reservas += 1
        self.save()

    def calcular_precio_venta(self):
        costo_hora_trabajo = 30
        precio_venta = self.duracion * costo_hora_trabajo + self.precio
        return precio_venta

    def obtener_servicios_similares(self):
        servicios_similares = Servicio.objects.filter(categoria=self.categoria).exclude(id=self.id)
        servicios_similares = servicios_similares.order_by('-numero_reservas')[:5]
        return servicios_similares
