from django.urls import path
from . import views

urlpatterns = [
    path("", views.formularioContacto, name="formularioContacto"),
    path("contactenos", views.contactenos, name="contactenos"),
]
