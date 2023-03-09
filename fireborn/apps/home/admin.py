from django.contrib import admin

# Register your models here.
from .models import Pricing

class PricingAdmin(admin.ModelAdmin):
    list_display = ('nombre_plan', 'precio', 'descripcion','duracion', 'numero_suscripciones', 'plan_popular')
    list_filter = ('duracion', 'plan_popular')
    search_fields = ('nombre_plan',)

admin.site.register(Pricing, PricingAdmin)
