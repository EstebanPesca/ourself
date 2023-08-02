from django.urls import path, include
from .api.views import UserLoginView
from .api.routers import router

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('', include(router.urls)),
]