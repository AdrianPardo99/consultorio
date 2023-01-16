from datetime import datetime

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.mixins import MultiSerializerViewSetMixin
from ..pagination import DefaultLimitOffsetPagination

from .serializers import (
    CitaCreateSerializer,
    CitaDetailSerializer,
    CitaUpdateSerializer,
)

from modelos.models import Cita


class CitaViewSet(
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
        "list": CitaDetailSerializer,
        "retrieve": CitaDetailSerializer,
        "create": CitaCreateSerializer,
        "partial_update": CitaUpdateSerializer,
    }
    lookup_url_kwarg = "cita_pk"
    lookup_field = "pk"
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Create cita
        ---
        example:
            {}
        """
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            output_serializer = CitaDetailSerializer(
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
        return super(CitaViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Delete cita
        ---
        example:
            {}
        """
        return super(CitaViewSet, self).destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        Lists all citas
        ---
        example:
            {}
        """
        return super(CitaViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retreive cita
        ---
        example:
            {}
        """
        return super(CitaViewSet, self).retrieve(request, *args, **kwargs)

    def get_queryset(self, pk=None):
        citas = Cita.objects.all()
        fecha = self.request.query_params.get("fecha")
        if pk:
            citas = get_object_or_404(citas, pk=pk)
        if fecha:
            # Parse fecha as date only for filter by date and not datetime as save in model
            fecha = datetime.fromisoformat(fecha)
            citas = citas.filter(fecha__date=fecha)
            if not citas:
                raise Http404
        return citas


cita_list = CitaViewSet.as_view(
    {
        "post": "create",
        "get": "list",
    }
)
cita_detail = CitaViewSet.as_view(
    {
        "get": "retrieve",
        "patch": "partial_update",
        "delete": "destroy",
    }
)
