from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('tienda', tienda, name="tienda"),
    path('nosotros', nosotros, name="nosotros"),
    path('ubicacion', ubicacion, name="ubicacion"),
    path('repuestos', repuestos, name="repuestos")
]