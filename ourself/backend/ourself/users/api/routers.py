from rest_framework.routers import DefaultRouter
from users.api.views import UserRegisterSet

router = DefaultRouter()

router.register(r'register', viewset=UserRegisterSet, basename='register')