from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id','first_name','last_name','username','email']

class UserSerializerPrueba(ModelSerializer):
    class Meta:
        model= User
        fields='__all__'
