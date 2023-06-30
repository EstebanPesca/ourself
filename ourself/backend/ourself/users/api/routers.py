from rest_framework.routers import DefaultRouter
from users.api.views import UserViewSet

router = DefaultRouter()

router.register(prefix='get/users',basename='user',viewset=UserViewSet)