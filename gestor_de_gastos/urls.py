from django.contrib import admin
from django.urls import path, include
from gastos.views import home  # Importar la vista de Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # ✅ Página de Inicio
    path('gastos/', include('gastos.urls')),  # ✅ URLs de Gastos
    path('ingresos/', include('ingresos.urls')),  # ✅ URLs de Ingresos
]

