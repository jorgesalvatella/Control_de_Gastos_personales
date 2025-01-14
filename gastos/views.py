from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Gasto

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Bienvenido a la aplicación de gestión de gastos</h1>")


def agregar_gasto(request):
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        categoria = request.POST.get('categoria')
        monto = request.POST.get('monto')
        descripcion = request.POST.get('descripcion')

        # Guardar el gasto en la base de datos
        Gasto.objects.create(
            fecha=fecha,
            categoria=categoria,
            monto=monto,
            descripcion=descripcion
        )

        return HttpResponseRedirect('/')

    # Obtener todos los gastos
    gastos = Gasto.objects.all()

    return render(request, 'gastos/agregar_gasto.html', {'gastos': gastos})
