from django.http import JsonResponse
from django.conf import settings

from rest_framework import renderers, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def welcome(request):
    data = {
        "name": "Proyecto de backend",
        "version": "0.0.1",
        "web": settings.API_URL,
    }
    return Response(data, status=status.HTTP_200_OK)


# Generic view to be used as handler_404 in urls
# https://docs.djangoproject.com/en/4.1/topics/http/views/#customizing-error-views


def not_found_request(request, exception, *args, **kwargs):
    """
    Generic 404 error handler.
    """
    data = {"error": "Not Found (404)"}
    return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)
