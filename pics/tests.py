from django.test import TestCase
from .models import Image,Location,Category

class ImageTestClass(TestCase):

    #set up method
    def setUp(self):
        self.mango = image(name = 'mango',description = 'yummy juicy')

    #testing instances
    def test_instance(self):
        self.assertTrue(isinstance(self.mango,image))     