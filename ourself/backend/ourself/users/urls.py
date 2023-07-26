from django.urls import path
from .api.views import UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
]