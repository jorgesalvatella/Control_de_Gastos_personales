from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# ✅ Redirigir "/" a "gastos/"
def home_redirect(request):
    return redirect('agregar_gasto')  # O usa 'agregar_ingreso'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gastos/', include('gastos.urls')),
    path('ingresos/', include('ingresos.urls')),
    path('', home_redirect, name='home'),  # 🔹 Redirige "/" a gastos
]
