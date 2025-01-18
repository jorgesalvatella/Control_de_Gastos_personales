from django.urls import path
from .views import agregar_ingreso, eliminar_ingreso

# ✅ Definir el `app_name` para evitar conflictos de nombres
app_name = 'ingresos'

urlpatterns = [
    path('', agregar_ingreso, name='agregar_ingreso'),  # Página para agregar ingresos
    path('eliminar/<int:ingreso_id>/', eliminar_ingreso, name='eliminar_ingreso'),  # Ruta para eliminar ingresos
]
