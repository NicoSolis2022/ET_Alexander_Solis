from django.urls import path
from base import views

urlpatterns= [
    path('index', views.index, name="index"),
    path('acercade', views.acercade, name="acercade"),
    path('api', views.api, name="api"),
    path('galeria', views.galeria, name="galeria"),
    path('Registro2', views.Registro2, name="Registro2"),
    path('formulario1', views.formulario1, name="formulario1"),
    path('registrarUsuario', views.registrarUsuario, name="registrarUsuario"),
]