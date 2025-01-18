from django.urls import path
from .views import agregar_gasto, eliminar_gasto, revisar_resultados

app_name = 'gastos'  # 🔥 Define el namespace para evitar conflictos

urlpatterns = [
    path('', agregar_gasto, name='agregar_gasto'),  # Página principal de gastos
    path('eliminar/<int:gasto_id>/', eliminar_gasto, name='eliminar_gasto'),  # Eliminar gasto
    path('resultados/', revisar_resultados, name='revisar_resultados'),  # Página de resultados
]
