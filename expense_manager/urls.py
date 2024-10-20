# expense_manager/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expenses/', include('expenses.urls')),  # Correctly include the expenses app URLs
]
