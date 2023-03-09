from django.db import models


class Pricing(models.Model):
    nombre_plan = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.CharField(max_length=20)
    descripcion = models.TextField()

    numero_suscripciones = models.PositiveIntegerField(default=0)
    plan_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_plan

    class Meta:
        ordering = ['precio']

    def aumentar_suscripciones(self):
        self.numero_suscripciones += 1
        self.save()

    def marcar_como_popular(self):
        precios = Pricing.objects.all()
        for precio in precios:
            precio.plan_popular = False
            precio.save()
        self.plan_popular = True
        self.save()

    def obtener_planes_populares(self):
        planes_populares = Pricing.objects.filter(plan_popular=True)
        return planes_populares

