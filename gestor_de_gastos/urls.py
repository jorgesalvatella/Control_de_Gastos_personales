from django.contrib import admin
from django.urls import path, include
from gastos.views import home  # ✅ Importamos la vista de inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # ✅ Página principal
    path('gastos/', include('gastos.urls', namespace='gastos')),  # ✅ Namespace correcto
    path('ingresos/', include('ingresos.urls', namespace='ingresos')),  # ✅ Namespace correcto
]
