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
    






# from rest_framework.response import Response
# from rest_framework.decorators import APIView

# from django.contrib.auth.models import User
# from users.api.serializers import UserSerializer

# @api_view(['GET'])
# def getUsers(request):
#     user=User.objects.all()
#     serializer=UserSerializer(user, many=True)
#     return Response(serializer.data)


# from django.contrib.auth.models import User
# from rest_framework import viewsets, permissions
# from users.api.serializers import UserSerializer

# class UsersViewSet(viewsets.ModelViewSet):
#     queryset=User.objects.all().order_by('-date_joined')
#     serializer_class=UserSerializer
#     permission_classes=[permissions.IsAuthenticated]

# class UserViewSet(viewsets.ModelViewSet):
#     def UserGet(pk):
#         queryset=User.objects.get(id=pk)
#         serializer_class=UserSerializer
#         permissions_classes=[permissions.IsAuthenticated]