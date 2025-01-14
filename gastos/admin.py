from django.contrib import admin

# Register your models here.



from django.contrib import admin
from .models import Gasto, Ingreso

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'categoria', 'monto', 'descripcion')

@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'fuente', 'monto', 'descripcion')
