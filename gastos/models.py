from django.db import models

class Gasto(models.Model):
    CATEGORIAS_GASTOS = [
        ('Alimentos', 'Alimentos'),
        ('Bebidas', 'Bebidas'),
        ('Hogar', 'Hogar'),
        ('Transporte', 'Transporte'),
        ('Salud', 'Salud'),
        ('Entretenimiento', 'Entretenimiento'),
        ('Otros', 'Otros'),
    ]
    fecha = models.DateField()  # Fecha elegida por el usuario
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Se asigna automáticamente al guardar
    categoria = models.CharField(max_length=50, choices=CATEGORIAS_GASTOS)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.fecha} (Ingresado el {self.fecha_registro}) - {self.categoria} - {self.monto}"


class Ingreso(models.Model):
    CATEGORIAS_INGRESOS = [
        ('Salario', 'Salario'),
        ('Negocios', 'Negocios'),
        ('Inversiones', 'Inversiones'),
        ('Regalos', 'Regalos'),
        ('Otros', 'Otros'),
    ]
    fecha = models.DateField()  # Fecha elegida por el usuario
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Se asigna automáticamente al guardar
    fuente = models.CharField(max_length=50, choices=CATEGORIAS_INGRESOS)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.fecha} (Ingresado el {self.fecha_registro}) - {self.fuente} - {self.monto}"

