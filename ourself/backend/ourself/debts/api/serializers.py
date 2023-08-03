from rest_framework import serializers
from ..models import Debt

class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = [
            'id', 'user', 'title', 'amount', 'category' ,'description'
            ]