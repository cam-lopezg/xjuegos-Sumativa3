"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('agregar-al-carrito/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/cantidad/', views.obtener_cantidad_carrito, name='obtener_cantidad_carrito'),
     path('carrito/limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
    path('carrito/pagar/', views.pagar_carrito, name='pagar_carrito'),
    path('editarperfil', views.editar_perfil, name='editarperfil'),
    path('Logout', views.logout_view, name='logout'),
    path("", views.index, name="index"),
    path("formin/", views.login_view, name="formin"),
    path("Login/", views.login, name="login"),
    path("juego5dos/", views.juego5dos, name="juego5dos"),
    path("juego5/", views.juego5, name="juego5"),
    path("juego4dos/", views.juego4dos, name="juego4dos"),
    path("juego4/", views.juego4, name="juego4"),
    path("juego3dos/", views.juego3dos, name="juego3dos"),
    path("juego3/", views.juego3, name="juego3"),
    path("juego2dos/", views.juego2dos, name="juego2dos"),
    path("juego2/", views.juego2, name="juego2"),
    path("juego1dos/", views.juego1dos, name="juego1dos"),
    path("juego1/", views.juego1, name="juego1"),
    path("Form/", views.form, name="form"),
    path("Categoria5/", views.categoria5, name="categoria5"),
    path("Categoria4/", views.categoria4, name="categoria4"),
    path("Categoria3/", views.categoria3, name="categoria3"),
    path("Categoria2/", views.categoria2, name="categoria2"),
    path("Categoria1/", views.categoria1, name="categoria1"),
    path("carrito/", views.carrito, name="carrito"),
    path("create_user/", views.create_user, name="create_user"),
    path("edit_user/", views.edit_user, name="edit_user"),
    path("delete_user/", views.delete_user, name="delete_user"),
    path("vista-restringida/", views.vista_restringida, name="vista_restringida"),
    path("principal/", views.principal, name="home"),
]
