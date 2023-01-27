from rest_framework import serializers
from core.user.models import PetStore


class PetStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetStore
        fields = ['id', 'game_id', 'model_id',
                  'order', 'lvl', 'pv', 'mana', 'exp']
