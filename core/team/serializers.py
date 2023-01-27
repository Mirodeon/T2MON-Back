from rest_framework import serializers
from core.user.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'game_id', 'model_id',
                  'order', 'lvl', 'pv', 'mana', 'exp']
