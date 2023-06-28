from rest_framework import routers
from users.api import views

router = routers.DefaultRouter()

router.register(r'', views.UserViewSet)