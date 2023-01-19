import ast

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

    def validate_pa(self, pa):
        if isinstance(pa, set):
            pa = list(pa)
        return str(pa)

    def validate_af(self, af):
        if isinstance(af, set):
            af = list(af)
        return str(af)

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
    pa = serializers.SerializerMethodField()
    af = serializers.SerializerMethodField()

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

    def get_pa(self, obj):
        return list(ast.literal_eval(obj.pa))

    def get_af(self, obj):
        return list(ast.literal_eval(obj.af))


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