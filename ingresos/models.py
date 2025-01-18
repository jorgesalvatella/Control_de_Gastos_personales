from django.db import models

class Ingreso(models.Model):
    fecha = models.DateField()
    fuente = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fuente} - {self.monto}"
