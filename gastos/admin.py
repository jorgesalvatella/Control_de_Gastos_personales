from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Gasto

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'categoria', 'monto', 'descripcion')
