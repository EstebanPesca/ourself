# Auth Users

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Register Users

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from users.api.serializers import UserSerializer
from rest_framework import viewsets


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({'access_token': access_token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        

class UserRegisterSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset=User.objects.all()
        serializer=UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        queryset=request.data
        serializer=UserSerializer(data=queryset)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def retrieve(self,request,pk):
        queryset=User.objects.all()
        user=get_object_or_404(queryset, pk=pk)
        serializer=UserSerializer(user)
        return Response(serializer.data)
    
    def update(self, request, pk):
        queryset=request.data
        user=User.objects.get(id=pk)
        serializer=UserSerializer(instance=user, data=queryset)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        user = User.objects.get(id=pk)
        user.delete()
        return Response('User deleted')
        