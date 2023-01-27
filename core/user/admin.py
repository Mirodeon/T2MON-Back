from django.contrib import admin
from .models import User, Game, Team, PetStore, Bag, PDF


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['email', 'username']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    search_fields = ['user_id__email', 'user_id__username']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    search_fields = ['game_id__user_id__email', 'game_id__user_id__username']


@admin.register(PetStore)
class PetStoreAdmin(admin.ModelAdmin):
    search_fields = ['game_id__user_id__email', 'game_id__user_id__username']


@admin.register(Bag)
class BagAdmin(admin.ModelAdmin):
    search_fields = ['game_id__user_id__email', 'game_id__user_id__username']


@admin.register(PDF)
class PDFAdmin(admin.ModelAdmin):
    search_fields = ['name']
