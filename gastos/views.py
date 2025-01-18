from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Gasto, Ingreso

# ✅ Vista principal (Página de Inicio)
def home(request):
    return render(request, 'home.html')  # Renderiza la página principal


# ✅ Vista para agregar un gasto
def agregar_gasto(request):
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        categoria = request.POST.get('categoria')
        monto = request.POST.get('monto')
        descripcion = request.POST.get('descripcion')

        # Validar campos obligatorios
        if not fecha or not categoria or not monto:
            return render(request, 'gastos/agregar_gasto.html', {
                'error': 'Todos los campos obligatorios deben ser completados.'
            })

        # Guardar el gasto en la base de datos
        nuevo_gasto = Gasto.objects.create(
            fecha=fecha,
            categoria=categoria,
            monto=monto,
            descripcion=descripcion
        )
        print(f"Gasto guardado: {nuevo_gasto}")  # Depuración

        return redirect('agregar_gasto')  # ✅ Redirige a la página de gastos

    # Obtener solo los últimos 10 gastos
    gastos = Gasto.objects.all().order_by('-fecha')[:10]
    return render(request, 'gastos/agregar_gasto.html', {'gastos': gastos})


# ✅ Vista para agregar un ingreso
def agregar_ingreso(request):
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        fuente = request.POST.get('fuente')
        monto = request.POST.get('monto')
        descripcion = request.POST.get('descripcion')

        # Validar campos obligatorios
        if not fecha or not fuente or not monto:
            return render(request, 'ingresos/agregar_ingreso.html', {
                'error': 'Todos los campos obligatorios deben ser completados.'
            })

        # Crear el ingreso en la base de datos
        nuevo_ingreso = Ingreso.objects.create(
            fecha=fecha,
            fuente=fuente,
            monto=monto,
            descripcion=descripcion
        )
        print(f"Ingreso guardado: {nuevo_ingreso}")  # Depuración

        return redirect('agregar_ingreso')  # ✅ Redirige a la página de ingresos

    # Obtener solo los últimos 10 ingresos
    ingresos = Ingreso.objects.all().order_by('-fecha')[:10]
    return render(request, 'ingresos/agregar_ingreso.html', {'ingresos': ingresos})


# ✅ Función para verificar si el usuario es administrador
def es_admin(user):
    return user.is_authenticated and user.is_staff


# ✅ Vista para eliminar un gasto (solo administradores)
@login_required
@user_passes_test(es_admin)
def eliminar_gasto(request, gasto_id):
    gasto = get_object_or_404(Gasto, id=gasto_id)
    gasto.delete()
    return redirect('agregar_gasto')  # ✅ Redirige a la lista de gastos después de eliminar


# ✅ Vista para eliminar un ingreso (solo administradores)
@login_required
@user_passes_test(es_admin)
def eliminar_ingreso(request, ingreso_id):
    ingreso = get_object_or_404(Ingreso, id=ingreso_id)
    ingreso.delete()
    return redirect('agregar_ingreso')  # ✅ Redirige a la lista de ingresos después de eliminar
