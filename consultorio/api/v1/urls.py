from django.urls import include, path

from .paciente import views as paciente_views
from .cita import views as cita_views

urlpatterns = [
    path(
        "pacientes/",
        paciente_views.paciente_list,
        name="pacientes",
    ),
    path(
        "pacientes/<paciente_pk>/",
        paciente_views.paciente_detail,
        name="paciente",
    ),
    path(
        "citas/",
        cita_views.cita_list,
        name="citass",
    ),
    path(
        "citas/<cita_pk>/",
        cita_views.cita_detail,
        name="cita",
    ),
]