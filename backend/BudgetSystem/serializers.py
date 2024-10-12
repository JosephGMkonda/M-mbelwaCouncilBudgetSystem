from rest_framework import serializers
from .models import Revenue,Department,BudgetSubmission,BudgetItem,BudgetAllocation


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = ['id','amount','month','collected_at','collected_by']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','name']

class BudgetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetItem

        fields =['id','submission','name','cost']

class BudgetSubmissionSerializer(serializers.ModelSerializer):
     items = BudgetItemSerializer(many=True, read_only=True)
     class Meta:
        model = BudgetSubmission
          
        fields = ['id', 'department', 'total_amount', 'submitted_by', 'submitted_at', 'items']


class BudgetAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetAllocation
        fields = ['id', 'department', 'allocated_amount', 'revenue', 'allocated_at', 'allocated_by']
