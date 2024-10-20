# expenses/urls.py

from django.urls import path
from .views import ExpenseListCreateView, ExpenseDetailView

urlpatterns = [
    path('', ExpenseListCreateView.as_view(), name='expense-list-create'),  # URL for listing and creating expenses
    path('<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),  # URL for viewing, updating, and deleting a specific expense
]
