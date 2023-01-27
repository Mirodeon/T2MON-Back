from rest_framework import serializers
from core.user.models import Bag


class BagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = ['id', 'game_id', 'model_id', 'order', 'amount']
