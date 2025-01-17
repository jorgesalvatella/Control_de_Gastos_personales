from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Gasto, Ingreso

# Vista principal
def index(request):
    return HttpResponse("<h1>Bienvenido a la aplicación de gestión de gastos e ingresos</h1>")

# Vista para agregar un gasto
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
        print(f"Gasto guardado: {nuevo_gasto}")  # Depuración para confirmar

        return HttpResponseRedirect('/')

    # Obtener solo los últimos 10 gastos
    gastos = Gasto.objects.all().order_by('-fecha')[:10]

    return render(request, 'gastos/agregar_gasto.html', {'gastos': gastos})


# Vista para agregar un ingreso
def agregar_ingreso(request):
    if request.method == 'POST':
        fecha = request.POST.get('fecha')  # Recoge la fecha enviada desde el formulario
        fuente = request.POST.get('fuente')
        monto = request.POST.get('monto')
        descripcion = request.POST.get('descripcion')

        # Validar campos obligatorios
        if not fecha or not fuente or not monto:
            return render(request, 'gastos/agregar_ingreso.html', {
                'error': 'Todos los campos obligatorios deben ser completados.'
            })

        # Crear el ingreso en la base de datos
        Ingreso.objects.create(
            fecha=fecha,
            fuente=fuente,
            monto=monto,
            descripcion=descripcion
        )
        return redirect('/ingresos/')  # Redirige al listado de ingresos

    # Obtener solo los últimos 10 ingresos
    ingresos = Ingreso.objects.all().order_by('-fecha')[:10]

    return render(request, 'gastos/agregar_ingreso.html', {'ingresos': ingresos})



