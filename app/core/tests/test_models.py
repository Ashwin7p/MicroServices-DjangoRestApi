from django.test import TestCase 
from django.contrib.auth import get_user_model #gets default user model configured for the project

class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )# fails becuse default user model requires a username by default, get_user_model acts as a manager

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))