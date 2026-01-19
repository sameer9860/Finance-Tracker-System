from django.urls import path
from .views import BudgetListCreateView, BudgetDetailView

urlpatterns = [
    path('', BudgetListCreateView.as_view(), name='budget-list-create'),
    path('<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),
]
