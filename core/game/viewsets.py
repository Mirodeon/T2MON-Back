from rest_framework import viewsets
from core.user.models import Game
from core.game.serializers import GameSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated']
    ordering = ['-updated']

    def get_queryset(self):
        user = self.request.user
        return Game.objects.filter(user_id=user)
