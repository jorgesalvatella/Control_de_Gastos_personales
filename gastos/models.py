from django.db import models

# Create your models here.
from django.db import models

class Gasto(models.Model):
    fecha = models.DateField()
    categoria = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.fecha} - {self.categoria} - {self.monto}"


        from django.db import models


class Ingreso(models.Model):
    fecha = models.DateField()
    fuente = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.fecha} - {self.fuente} - {self.monto}"

