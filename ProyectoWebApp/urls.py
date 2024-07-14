from django.urls import path
from . import views

from  ProyectoWebApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="Home"),
    path('tienda/', views.tienda, name='Tienda'),
    path('listar-productos/', views.listar_productos, name='listar_productos'),
    
    


]

urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)