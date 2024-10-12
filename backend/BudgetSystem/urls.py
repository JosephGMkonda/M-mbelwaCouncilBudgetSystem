# budget_system/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Revenue endpoints
    path('revenues/', views.revenue_list, name='revenue-list'),
    path('revenues/<int:pk>/', views.revenue_detail, name='revenue-detail'),
    
    # Department endpoints
    path('departments/', views.department_list, name='department-list'),
    path('departments/<int:pk>/', views.department_detail, name='department-detail'),
    
    # Budget Submission endpoints
    path('budget-submissions/', views.budget_submission_list, name='budget-submission-list'),
    path('budget-submissions/<int:pk>/', views.budget_submission_detail, name='budget-submission-detail'),
    
    # Budget Item endpoints
    path('budget-items/', views.budget_item_list, name='budget-item-list'),
    path('budget-items/<int:pk>/', views.budget_item_detail, name='budget-item-detail'),
    
    # Budget Allocation endpoints
    path('budget-allocations/', views.budget_allocation_list, name='budget-allocation-list'),
    path('budget-allocations/<int:pk>/', views.budget_allocation_detail, name='budget-allocation-detail'),
]
