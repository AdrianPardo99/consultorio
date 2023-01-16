from rest_framework import serializers

from modelos.models import Paciente
from modelos import ProblemasActuales, AntecedenteFamiliares


class UsuarioCreateSerializer(serializers.ModelSerializer):
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


class UsuarioDetailSerializer(serializers.ModelSerializer):
    pa = serializers.CharField(source="get_pa_display")
    af = serializers.CharField(source="get_af_display")

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


class UsuarioUpdateSerializer(serializers.ModelSerializer):
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