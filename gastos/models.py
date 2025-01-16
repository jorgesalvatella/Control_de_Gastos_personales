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
    fecha = models.DateField()
    categoria = models.CharField(max_length=50, choices=CATEGORIAS_GASTOS)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.fecha} - {self.categoria} - {self.monto}"

class Ingreso(models.Model):
    CATEGORIAS_INGRESOS = [
        ('Salario', 'Salario'),
        ('Negocios', 'Negocios'),
        ('Inversiones', 'Inversiones'),
        ('Regalos', 'Regalos'),
        ('Otros', 'Otros'),
    ]
    fecha = models.DateField()
    fuente = models.CharField(max_length=50, choices=CATEGORIAS_INGRESOS)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.fecha} - {self.fuente} - {self.monto}"
