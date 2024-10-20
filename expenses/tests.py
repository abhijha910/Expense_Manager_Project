# expenses/tests.py
from django.test import TestCase
from .models import User, Expense

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name='John Doe', email='john@example.com')

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'John Doe')
 
