from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Revenue, Department, BudgetSubmission, BudgetItem, BudgetAllocation
from .serializers import (
    RevenueSerializer,
    DepartmentSerializer,
    BudgetSubmissionSerializer,
    BudgetItemSerializer,
    BudgetAllocationSerializer,
)


# Revenue Views
@api_view(['GET', 'POST'])
def revenue_list(request):
    if request.method == 'GET':
        revenues = Revenue.objects.all()
        serializer = RevenueSerializer(revenues, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RevenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def revenue_detail(request, pk):
    try:
        revenue = Revenue.objects.get(pk=pk)
    except Revenue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RevenueSerializer(revenue)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RevenueSerializer(revenue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        revenue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Department Views
@api_view(['GET', 'POST'])
def department_list(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def department_detail(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Budget Submission Views
@api_view(['GET', 'POST'])
def budget_submission_list(request):
    if request.method == 'GET':
        submissions = BudgetSubmission.objects.all()
        serializer = BudgetSubmissionSerializer(submissions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BudgetSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def budget_submission_detail(request, pk):
    try:
        submission = BudgetSubmission.objects.get(pk=pk)
    except BudgetSubmission.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BudgetSubmissionSerializer(submission)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BudgetSubmissionSerializer(submission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        submission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Budget Item Views
@api_view(['GET', 'POST'])
def budget_item_list(request):
    if request.method == 'GET':
        items = BudgetItem.objects.all()
        serializer = BudgetItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BudgetItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def budget_item_detail(request, pk):
    try:
        item = BudgetItem.objects.get(pk=pk)
    except BudgetItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BudgetItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BudgetItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Budget Allocation Views
@api_view(['GET', 'POST'])
def budget_allocation_list(request):
    if request.method == 'GET':
        allocations = BudgetAllocation.objects.all()
        serializer = BudgetAllocationSerializer(allocations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BudgetAllocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def budget_allocation_detail(request, pk):
    try:
        allocation = BudgetAllocation.objects.get(pk=pk)
    except BudgetAllocation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BudgetAllocationSerializer(allocation)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BudgetAllocationSerializer(allocation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        allocation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
