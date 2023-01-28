from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view


@api_view(['GET'])
def HealthCheck(self):
    return Response(status=status.HTTP_200_OK)
