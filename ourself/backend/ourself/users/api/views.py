from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
from users.api.serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset=User.objects.all()
        serializer=UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk):
        queryset=User.objects.all()
        user=get_object_or_404(queryset, pk=pk)
        serializer=UserSerializer(user)
        return Response(serializer.data)
    
    def create(self, request):
        queryset=request.data
        serializer=UserSerializer(data=queryset)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
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