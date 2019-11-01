from django.test import TestCase

from .models import Profile
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.bio= Profile(bio = 'software')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.bio,Profile))
