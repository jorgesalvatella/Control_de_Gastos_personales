

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
