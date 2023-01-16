# Django standard
from django.db import models

# Local and own modules
from core.models import BaseModel, SoftDeletionManager
from . import ProblemasActuales, AntecedenteFamiliares


class Paciente(BaseModel):
    nombre = models.CharField("Nombre", blank=False, null=False, max_length=255)
    ap = models.CharField("Apellido paterno", blank=False, null=False, max_length=255)
    am = models.CharField("Apellido materno", blank=False, null=False, max_length=255)
    edad = models.IntegerField("Edad", blank=False, null=False)
    peso = models.DecimalField(
        "Peso", blank=False, null=False, decimal_places=2, max_digits=6
    )
    estatura = models.DecimalField(
        "Estatura", blank=False, null=False, decimal_places=2, max_digits=6
    )
    cc = models.DecimalField(
        "Circunferencia de cintura",
        blank=False,
        null=False,
        decimal_places=2,
        max_digits=6,
    )
    telefono = models.CharField("Télefono", blank=False, null=False, max_length=20)
    email = models.EmailField("Email / Correo electronico", blank=False, null=False)
    pa = models.CharField(
        "Problemas actuales",
        blank=False,
        null=False,
        choices=ProblemasActuales.CHOICES,
        max_length=255,
    )
    af = models.CharField(
        "Antecedentes familiares",
        blank=False,
        null=False,
        choices=AntecedenteFamiliares.CHOICES,
        max_length=255,
    )
    ea = models.BooleanField("Embarazo actual", null=False)

    def __str__(self) -> str:
        return "{} {} {} - {} / {}".format(
            self.nombre, self.ap, self.am, self.email, self.telefono
        )

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        db_table = "paciente"


class Cita(BaseModel):
    paciente = models.ForeignKey(
        Paciente,
        verbose_name="paciente",
        on_delete=models.PROTECT,
        related_name="citas",
    )
    fecha = models.DateTimeField("Fecha y horario de cita", null=False, blank=False)

    def __str__(self) -> str:
        return "{} Cita: {}".format(self.paciente, self.fecha)

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        db_table = "cita"
