from django.urls import path
from .views import agregar_gasto, eliminar_gasto

urlpatterns = [
    path('', agregar_gasto, name='agregar_gasto'),  # Página para agregar gastos
    path('eliminar/<int:gasto_id>/', eliminar_gasto, name='eliminar_gasto'),  # Ruta para eliminar gastos
]


