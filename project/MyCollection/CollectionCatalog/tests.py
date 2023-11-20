from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Collection,CollectionObject,Book,Watch,Category

class CollectionObjectModelTest(TestCase):
    def test_create_collection_object(self):
        obj=CollectionObject.objects.create(name='Test object',description='Test description')
        self.assertEqual(obj.name,'Test object')
        self.assertEqual(obj.description,'Test description')

class BookModelTest(TestCase):
    def test_create_book(self):
        book=Book.objects.create(name='Test Book',description='Test description',author='Test Author',type='RM')
        self.assertEqual(book.name,'Test Book')
        self.assertEqual(book.description,'Test description')
        self.assertEqual(book.author,'Test Author')
        self.assertEqual(book.type,'RM')
    
class WatchModelTest(TestCase):
    def test_create_watch(self):
        watch=Watch.objects.create(name='Test Watch',description='Test description',type_of_mecanism='MM')
        self.assertEqual(watch.name,'Test Watch')  
        self.assertEqual(watch.description,'Test description')
        self.assertEqual(watch.type_of_mecanism,'MM')
        
        
class CategoryModelTest(TestCase):
    def test_create_category(self):
        category=Category.objects.create(name='Test Category')
        self.assertEqual(category.name,'Test Category')
        
class CollectionModelTest(TestCase):
    def setUp(self):
        self.test_category=Category.objects.create(name='Test Category')
        self.test_collection_object=CollectionObject.objects.create(name='Test Object',description='Test Description')
        self.test_book=Book.objects.create(name='Test Book',description='Test Description',author='Test Author',type='RM')
        self.test_watch=Watch.objects.create(name='Test Watch',description='Test Description',type_of_mecanism='MM')
        
    def test_create_collection(self):
        collection=Collection.objects.create(name='Test Collection',category=self.test_category)
        self.assertEqual(collection.name,'Test Collection')
        self.assertEqual(collection.category,self.test_category)
        self.assertEqual(collection.collection_objects.count(),0)
    
    def test_add_objects_to_collection(self):
        collection=Collection.objects.create(name='Test Collection',category=self.test_category)
        collection.collection_objects.add(self.test_collection_object, self.test_book,self.test_watch)
        
        self.assertEqual(collection.collection_objects.count(),3)
        self.assertIn(self.test_collection_object,collection.collection_objects.all())
        self.assertIn(self.test_book,collection.collection_objects.all())
        self.assertIn(self.test_watch,collection.collection_objects.all())
        
    # def test_get_absolute_url(self):
    #     collection=Collection.objects.create(name='Test Collection',category=self.test_category)
    #     self.assertEqual(collection.get_absolute_url(),f'/collections/{collection.id}/')