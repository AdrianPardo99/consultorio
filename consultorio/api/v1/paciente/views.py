from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.mixins import MultiSerializerViewSetMixin
from ..pagination import DefaultLimitOffsetPagination

from .serializers import (
    PacienteCreateSerializer,
    PacienteDetailSerializer,
    PacienteUpdateSerializer,
)

from modelos.models import Paciente


class PacienteViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    MultiSerializerViewSetMixin,
    viewsets.GenericViewSet,
):
    pagination_class = DefaultLimitOffsetPagination
    serializer_action_classes = {
        "list": PacienteDetailSerializer,
        "retrieve": PacienteDetailSerializer,
        "create": PacienteCreateSerializer,
        "partial_update": PacienteUpdateSerializer,
    }
    lookup_url_kwarg = "paciente_pk"
    lookup_field = "pk"
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Create paciente
        ---
        example:
            {}
        """
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            output_serializer = PacienteDetailSerializer(
                instance, context={"request": request}
            )
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        """
        Update certain paciente
        ---
        example:
            {}
        """
        return super(PacienteViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Delete paciente
        ---
        example:
            {}
        """
        return super(PacienteViewSet, self).destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        Lists all pacientes.
        ---
        example:
            {}
        """
        return super(PacienteViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retreive paciente
        ---
        example:
            {}
        """
        return super(PacienteViewSet, self).retrieve(request, *args, **kwargs)

    def get_queryset(self, pk=None):
        pacientes = Paciente.objects.all()
        nombre = self.request.query_params.get("nombre")
        if pk:
            pacientes = get_object_or_404(pacientes, pk=pk)
        if nombre:
            pacientes = pacientes.filter(nombre__icontains=nombre)
            if not pacientes:
                raise Http404
        return pacientes


paciente_list = PacienteViewSet.as_view(
    {
        "post": "create",
        "get": "list",
    }
)
paciente_detail = PacienteViewSet.as_view(
    {
        "get": "retrieve",
        "patch": "partial_update",
        "delete": "destroy",
    }
)
