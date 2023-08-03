from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Debt
from .serializers import DebtSerializer

@api_view(['GET'])
def debt_list(request):
    debts = Debt.objects.filter(user=request.user)
    serializer = DebtSerializer(debts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def debt_detail(request, pk):
    try:
        debts=Debt.objects.get(id=pk, user=request.user)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = DebtSerializer(debts)
    return Response(serializer.data)

@api_view(['POST'])
def debt_create(request):
    serializer = DebtSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def debt_update(request, pk):
    try:
        debt = Debt.objects.get(pk=pk, user=request.user)
    except Debt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = DebtSerializer(debt, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def debt_delete(request, pk):
    try:
        debt = Debt.objects.get(pk=pk, user=request.user)
    except Debt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    debt.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)