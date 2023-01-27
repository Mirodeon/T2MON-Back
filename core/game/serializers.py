from rest_framework import serializers
from core.user.models import Game, Team, PetStore, Bag
from core.team.serializers import TeamSerializer
from core.petStore.serializers import PetStoreSerializer
from core.bag.serializers import BagSerializer


class GameSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=True)
    petStore = PetStoreSerializer(many=True)
    bag = BagSerializer(many=True)

    class Meta:
        model = Game
        fields = ['id', 'user_id', 'name', 'pseudo',
                  'position', 'gold', 'created', 'updated', 'team', 'petStore', 'bag']

    def create(self, validated_data):
        team = validated_data.pop('team')
        petStore = validated_data.pop('petStore')
        bag = validated_data.pop('bag')
        game_instance = Game.objects.create(**validated_data)
        for item in team:
            Team.objects.create(game_id=game_instance, **item)
        for item in petStore:
            PetStore.objects.create(game_id=game_instance, **item)
        for item in bag:
            Bag.objects.create(game_id=game_instance, **item)
        return game_instance

    def update(self, instance, validated_data):
        team = validated_data.pop('team')
        petStore = validated_data.pop('petStore')
        bag = validated_data.pop('bag')
        instance.name = validated_data.get('name', instance.name)
        instance.pseudo = validated_data.get('pseudo', instance.pseudo)
        instance.position = validated_data.get('position', instance.position)
        instance.gold = validated_data.get('gold', instance.gold)
        instance.save()

        """update Team"""
        team_with_same_game_instance = Team.objects.filter(
            game_id=instance.pk).values_list('id', flat=True)

        team_id_pool = []

        for item in team:
            if "id" in item.keys():
                if Team.objects.filter(id=item['id']).exists():
                    item_team_instance = Team.objects.get(id=item['id'])
                    item_team_instance.model_id = item.get(
                        'model_id', item_team_instance.model_id)
                    item_team_instance.order = item.get(
                        'order', item_team_instance.order)
                    item_team_instance.lvl = item.get(
                        'lvl', item_team_instance.lvl)
                    item_team_instance.pv = item.get(
                        'pv', item_team_instance.pv)
                    item_team_instance.mana = item.get(
                        'mana', item_team_instance.mana)
                    item_team_instance.exp = item.get(
                        'exp', item_team_instance.exp)
                    item_team_instance.save()
                    team_id_pool.append(item_team_instance.id)
                else:
                    continue
            else:
                team_instance = Team.objects.create(**item)
                team_id_pool.append(team_instance.id)

        for team_id in team_with_same_game_instance:
            if team_id not in team_id_pool:
                Team.objects.filter(pk=team_id).delete()

        """update PetStore"""
        petStore_with_same_game_instance = PetStore.objects.filter(
            game_id=instance.pk).values_list('id', flat=True)

        petStore_id_pool = []

        for item in petStore:
            if "id" in item.keys():
                if PetStore.objects.filter(id=item['id']).exists():
                    item_petStore_instance = PetStore.objects.get(
                        id=item['id'])
                    item_petStore_instance.model_id = item.get(
                        'model_id', item_petStore_instance.model_id)
                    item_petStore_instance.order = item.get(
                        'order', item_petStore_instance.order)
                    item_petStore_instance.lvl = item.get(
                        'lvl', item_petStore_instance.lvl)
                    item_petStore_instance.pv = item.get(
                        'pv', item_petStore_instance.pv)
                    item_petStore_instance.mana = item.get(
                        'mana', item_petStore_instance.mana)
                    item_petStore_instance.exp = item.get(
                        'exp', item_petStore_instance.exp)
                    item_petStore_instance.save()
                    petStore_id_pool.append(item_petStore_instance.id)
                else:
                    continue
            else:
                petStore_instance = PetStore.objects.create(**item)
                petStore_id_pool.append(petStore_instance.id)

        for petStore_id in petStore_with_same_game_instance:
            if petStore_id not in petStore_id_pool:
                PetStore.objects.filter(pk=petStore_id).delete()

        """update Bag"""
        bag_with_same_game_instance = Bag.objects.filter(
            game_id=instance.pk).values_list('id', flat=True)

        bag_id_pool = []

        for item in bag:
            if "id" in item.keys():
                if Bag.objects.filter(id=item['id']).exists():
                    item_bag_instance = Bag.objects.get(id=item['id'])
                    item_bag_instance.model_id = item.get(
                        'model_id', item_bag_instance.model_id)
                    item_bag_instance.order = item.get(
                        'order', item_bag_instance.order)
                    item_bag_instance.amount = item.get(
                        'amount', item_bag_instance.amount)
                    item_bag_instance.save()
                    bag_id_pool.append(item_bag_instance.id)
                else:
                    continue
            else:
                bag_instance = Bag.objects.create(**item)
                bag_id_pool.append(bag_instance.id)

        for bag_id in bag_with_same_game_instance:
            if bag_id not in bag_id_pool:
                Bag.objects.filter(pk=bag_id).delete()

        return instance
