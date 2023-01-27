from rest_framework.routers import SimpleRouter
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from core.game.viewsets import GameViewSet


routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet,
                basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'user', UserViewSet, basename='user')

# GAME
routes.register(r'game', GameViewSet, basename='game')


urlpatterns = [
    *routes.urls
]
