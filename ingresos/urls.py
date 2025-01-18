from django.urls import path
from .views import agregar_ingreso, eliminar_ingreso

urlpatterns = [
    path('', agregar_ingreso, name='agregar_ingreso'),
    path('eliminar/<int:ingreso_id>/', eliminar_ingreso, name='eliminar_ingreso'),
]
