from rest_framework import serializers

from modelos.models import Paciente
from modelos import ProblemasActuales, AntecedenteFamiliares


class PacienteCreateSerializer(serializers.ModelSerializer):
    pa = serializers.MultipleChoiceField(
        choices=ProblemasActuales.CHOICES, required=True
    )
    af = serializers.MultipleChoiceField(
        choices=AntecedenteFamiliares.CHOICES, required=True
    )

    class Meta:
        model = Paciente
        fields = (
            "nombre",
            "ap",
            "am",
            "edad",
            "peso",
            "estatura",
            "cc",
            "telefono",
            "email",
            "pa",
            "af",
            "ea",
        )


class PacienteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = (
            "id",
            "created_at",
            "nombre",
            "ap",
            "am",
            "edad",
            "peso",
            "estatura",
            "cc",
            "telefono",
            "email",
            "pa",
            "af",
            "ea",
        )


class PacienteUpdateSerializer(serializers.ModelSerializer):
    pa = serializers.MultipleChoiceField(
        choices=ProblemasActuales.CHOICES, required=True
    )
    af = serializers.MultipleChoiceField(
        choices=AntecedenteFamiliares.CHOICES, required=True
    )

    class Meta:
        model = Paciente
        fields = (
            "nombre",
            "ap",
            "am",
            "edad",
            "peso",
            "estatura",
            "cc",
            "telefono",
            "email",
            "pa",
            "af",
            "ea",
        )