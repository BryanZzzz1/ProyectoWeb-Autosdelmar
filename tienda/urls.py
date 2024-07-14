from django.urls import path
from . import views
from  tienda.views import *

app_name = 'tienda'


urlpatterns = [
    path('', tienda, name="Tienda"),
    path('', views.listar_productos, name='listar_productos'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('actualizar/<int:pk>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    
]
