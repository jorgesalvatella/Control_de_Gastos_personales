from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum
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

        return redirect('gastos:agregar_gasto')  # ✅ Redirige a la página de gastos

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

        return redirect('ingresos:agregar_ingreso')  # ✅ Redirige a la página de ingresos

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
    return redirect('gastos:agregar_gasto')  # ✅ Redirige a la lista de gastos después de eliminar


# ✅ Vista para eliminar un ingreso (solo administradores)
@login_required
@user_passes_test(es_admin)
def eliminar_ingreso(request, ingreso_id):
    ingreso = get_object_or_404(Ingreso, id=ingreso_id)
    ingreso.delete()
    return redirect('ingresos:agregar_ingreso')  # ✅ Redirige a la lista de ingresos después de eliminar


# 📊 ✅ Vista para revisar resultados financieros
def revisar_resultados(request):
    # Obtener parámetros de filtro
    filtro_fecha_inicio = request.GET.get('fecha_inicio')
    filtro_fecha_fin = request.GET.get('fecha_fin')
    filtro_tipo = request.GET.get('tipo')  # Puede ser 'gasto' o 'ingreso'
    filtro_categoria = request.GET.get('categoria')

    # Consultas base
    gastos = Gasto.objects.all()
    ingresos = Ingreso.objects.all()

    # Aplicar filtros si se especifican
    if filtro_fecha_inicio and filtro_fecha_fin:
        gastos = gastos.filter(fecha__range=[filtro_fecha_inicio, filtro_fecha_fin])
        ingresos = ingresos.filter(fecha__range=[filtro_fecha_inicio, filtro_fecha_fin])

    if filtro_tipo == 'gasto':
        ingresos = Ingreso.objects.none()  # Ocultar ingresos
    elif filtro_tipo == 'ingreso':
        gastos = Gasto.objects.none()  # Ocultar gastos

    if filtro_categoria:
        gastos = gastos.filter(categoria=filtro_categoria)
        ingresos = ingresos.filter(fuente=filtro_categoria)

    # Calcular totales
    total_gastos = gastos.aggregate(Sum('monto'))['monto__sum'] or 0
    total_ingresos = ingresos.aggregate(Sum('monto'))['monto__sum'] or 0
    saldo_total = total_ingresos - total_gastos

    context = {
        'gastos': gastos,
        'ingresos': ingresos,
        'total_gastos': total_gastos,
        'total_ingresos': total_ingresos,
        'saldo_total': saldo_total,
    }

    return render(request, 'resultados.html', context)  # ✅ Usa la plantilla global correcta
