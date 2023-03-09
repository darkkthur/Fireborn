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


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad_inventario = models.PositiveIntegerField()
    numero_ventas = models.PositiveIntegerField(default=0)
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['-numero_ventas']

    def aumentar_ventas(self):
        self.numero_ventas += 1
        self.save()

    def calcular_precio_venta(self):
        margen_ganancia = 0.3
        precio_venta = self.precio / (1 - margen_ganancia)
        return precio_venta

    def obtener_productos_similares(self):
        productos_similares = Producto.objects.filter(categoria=self.categoria).exclude(id=self.id)
        productos_similares = productos_similares.order_by('-numero_ventas')[:5]
        return productos_similares
