

from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]


urlpatterns = [
    path('', index, name='index'),
]
from django.urls import path
from .views import agregar_gasto

urlpatterns = [
    path('', agregar_gasto, name='agregar_gasto'),
]


from django.urls import path
from .views import agregar_gasto, agregar_ingreso

urlpatterns = [
    path('', agregar_gasto, name='agregar_gasto'),
    path('ingresos/', agregar_ingreso, name='agregar_ingreso'),
]
