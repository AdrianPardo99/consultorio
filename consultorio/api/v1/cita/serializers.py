from rest_framework import serializers

from modelos.models import Cita, Paciente

from ..paciente.serializers import PacienteDetailSerializer


class CitaCreateSerializer(serializers.ModelSerializer):
    paciente = serializers.CharField(required=True)

    class Meta:
        model = Cita
        fields = ("paciente", "fecha")

    def validate_paciente(self, paciente):
        paciente = Paciente.objects.filter(pk=paciente)
        if not paciente:
            raise serializers.ValidationError("Paciente no encontrado")
        return paciente.first()


class CitaDetailSerializer(serializers.ModelSerializer):
    paciente = PacienteDetailSerializer(read_only=True)

    class Meta:
        model = Cita
        fields = ("id", "paciente", "fecha")


class CitaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = "fecha"
