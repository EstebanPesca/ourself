from rest_framework.routers import DefaultRouter
from users.api.views import UserViewSet

router = DefaultRouter()

router.register(r'users', viewset=UserViewSet, basename='users')