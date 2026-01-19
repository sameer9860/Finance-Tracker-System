from django.urls import path
from .views import (
    BudgetListCreateView, BudgetDetailView,
    SavingsListCreateView, SavingsDetailView
)

urlpatterns = [
    path('', BudgetListCreateView.as_view(), name='budget-list-create'),
    path('<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),
    path('savings/', SavingsListCreateView.as_view(), name='savings-list-create'),
    path('savings/<int:pk>/', SavingsDetailView.as_view(), name='savings-detail'),
]
