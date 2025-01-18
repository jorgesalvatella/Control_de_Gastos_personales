from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingreso

def agregar_ingreso(request):
    if request.method == 'POST':
        fecha = request.POST['fecha']
        fuente = request.POST['fuente']
        monto = request.POST['monto']
        descripcion = request.POST['descripcion']
        Ingreso.objects.create(fecha=fecha, fuente=fuente, monto=monto, descripcion=descripcion)
        return redirect('agregar_ingreso')

    ingresos = Ingreso.objects.all().order_by('-fecha')
    return render(request, 'ingresos/agregar_ingreso.html', {'ingresos': ingresos})

def eliminar_ingreso(request, ingreso_id):
    ingreso = get_object_or_404(Ingreso, id=ingreso_id)
    ingreso.delete()
    return redirect('agregar_ingreso')
