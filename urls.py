from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from expenses.views import ExpenseViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
            