from rest_framework import serializers
from .models import Budget, Savings

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
        read_only_fields = ['user']

class SavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields = '__all__'
        read_only_fields = ['user']
