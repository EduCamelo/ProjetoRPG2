
from django.urls import path
from . import views

urlpatterns = [
    path('registro', views.registro , name='registro'),
    path('', views.personagem, name='personagem'),
    path('consulta', views.revConsulta, name='consulta'),
    path('luta1', views.luta1, name='luta1'),
    path('luta2', views.luta2, name='luta2'),
    path('luta3', views.luta3, name='luta3'),
    path('lutaFinal', views.lutaFinal, name='lutaFinal'),
    path('derrota', views.derrota, name='derrota')
]