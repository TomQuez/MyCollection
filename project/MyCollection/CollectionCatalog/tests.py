from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Collection,CollectionObject,Book,Watch,Category

class CollectionObjectModelTest(TestCase):
    def test_create_collection_object(self):
        obj=CollectionObject.objects.create(name='Test object',description='Test description')
        self.assertEqual(obj.name,'Test object')
        self.assertEqual(obj.description,'Test description')