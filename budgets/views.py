from rest_framework import generics, permissions
from .models import Budget, Savings
from .serializers import BudgetSerializer, SavingsSerializer

class BudgetListCreateView(generics.ListCreateAPIView):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BudgetDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)


class SavingsListCreateView(generics.ListCreateAPIView):
    serializer_class = SavingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Savings.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SavingsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SavingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Savings.objects.filter(user=self.request.user)
