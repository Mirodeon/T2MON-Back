from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from core.user.models import User


@api_view(['GET'])
def HealthCheck(self):
    if User.objects.filter(username='Admin').exists():
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
