"""
Tests for the Django admin modifications.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Tests for Django admin."""

    def setUp(self):
        """Create user and client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User'
        )

    def test_users_lists(self):
        """Test that users are listed on page."""
        url = reverse('admin:core_user_changelist')#url for views directly, in case url changes later
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self): #edit a user in gui
        """Test the edit user page works."""
        url = reverse('admin:core_user_change', args=[self.user.id])#url for views directly, in case url changes later
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self): #add new user page, customized fields
        """Test the create user page works."""
        url = reverse('admin:core_user_add') #url for views directly, in case url changes later
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)