from django.test import TestCase
from django.contrib.auth import get_user_model
from django.templatetags.static import static
import os
from users.models import UserProfile

User = get_user_model()
password = os.environ.get('TEST_PASSWORD')


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(email='testuser@test.com', password=password)
        self.assertEqual(user.email, 'testuser@test.com')
        self.assertTrue(user.check_password('testpass'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.role, 'user')

    def test_create_superuser(self):
        admin = User.objects.create_superuser(email='admin@test.com', password=password)
        self.assertEqual(admin.email, 'admin@test.com')
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)

    def test_email_required(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password=password)


class UserProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@test.com', password=password
        )
        self.profile = UserProfile.objects.create(
            user=self.user, first_name='John', last_name='Doe'
        )

    def test_email(self):
        self.assertEqual(self.profile.email, self.user.email)

    def test_str_method(self):
        expected_str = f'user_id={self.profile.id} email={self.user.email}'
        self.assertEqual(str(self.profile), expected_str)

    def test_get_avatar_url_with_avatar(self):
        self.profile.avatar = 'avatars/test_avatar.png'
        self.profile.save()
        self.assertIn('avatars/test_avatar.png', self.profile.get_avatar_url())

    def test_get_avatar_url_without_avatar(self):
        self.profile.avatar = None
        self.profile.save()
        self.assertEqual(
            self.profile.get_avatar_url(), static('placeholders/avatar-placeholder.png')
        )
