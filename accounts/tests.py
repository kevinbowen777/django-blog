from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse  # noqa:F401


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="kevin",
            email="kevin@example.com",
            password="T3stP@ss123!",
        )
        self.assertEqual(user.username, "kevin")
        self.assertEqual(user.email, "kevin@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="superadmin",
            email="superadmin@example.com",
            password="t3stP@ss123!",
        )
        self.assertEqual(user.username, "superadmin")
        self.assertEqual(user.email, "superadmin@example.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
