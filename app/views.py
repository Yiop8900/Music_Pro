from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def tienda(request):
    return render(request, 'tienda.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def ubicacion(request):
    return render(request, 'ubicacion.html')