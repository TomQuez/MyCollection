from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
import uuid

def validate_image_extension(value):
    if not value.name.endswith(('.jpg','.jpeg','.png','.gif')):
        raise ValidationError("Seuls les fichiers image .jpg, .jpeg, .png, .gif sont autorisés")

# Create your models here.
class Object(models.Model):
    """generic class that represent an object contained in a collection"""
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Unique ID for this particular object')
    name=models.CharField(max_length=200,help_text='Enter a name for your object,a title for your book, or the model of your watch')
    description=models.TextField(max_length=1500,help_text='Enter a brief description of your object')
    image=models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        """function required to manipulate an object"""
        return self.name
    def get_absolute_url(self):
        """function required to display the detail of an object"""
        return reverse('object-detail',args=[str(self.id)])
    
class Book (Object):
    """class that represent Books"""
    author=models.CharField(max_length=200,help_text='Enter the name of the author')
    TYPE_OF_BOOK=[
        ("RM","Roman"),
        ("MG","Manga"),
        ("ES","Essai"),
        ("BD","Bande Dessinée"),
        ("CS","Comics"),
        ("BL","Beau Livre"),
        ("AU","Autre"),
    ]
    type=models.CharField(max_length=2,choices=TYPE_OF_BOOK,help_text="choose the type of book")
    
class Watch (Object):
    """class that represents watches"""
    brand=models.CharField(max_length=100,help_text='enter the brand of your watch')
    Material=models.CharField(max_length=200,help_text='Enter the material(s) of your watch',blank=True, null=True)
    type_of_mecanism=models.CharField(max_length=100, help_text='Enter the type of mecanism of your watch, e.g. automatic',blank=True, null=True)
        
    
class Category(models.Model):
    """class that represent a category for a collection"""
    name=models.CharField(max_length=200,help_text='Enter the name of your category',unique=True)
    
    def __str__(self):
        return self.name
    
class Collection(models.Model):
    """class that represent a collection of objects"""
    name=models.CharField(max_length=200,help_text='Enter a name for your collection')
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)