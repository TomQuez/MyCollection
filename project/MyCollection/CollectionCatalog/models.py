from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
import uuid
from django.contrib.contenttypes.fields import GenericRelation

def validate_image_extension(value):
    if not value.name.endswith(('.jpg','.jpeg','.png','.gif')):
        raise ValidationError("Seuls les fichiers image .jpg, .jpeg, .png, .gif sont autorisés")

# Create your models here.
class CollectionObject(models.Model):
    """generic class that represent an object contained in a collection"""
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Unique ID for this particular object')
    name=models.CharField(max_length=200,help_text='Enter a name for your object,a title for your book, or the model of your watch')
    description=models.TextField(max_length=1500,help_text='Enter a brief description of your object')
    image=models.ImageField(upload_to='images/', null=True, blank=True,validators=[validate_image_extension])
    
   
    
    def __str__(self):
        """function required to manipulate an object"""
        return self.name
    def get_absolute_url(self):
        """function required to display the detail of an object"""
        return reverse('object-detail',args=[str(self.id)])
    
class Book (CollectionObject):
    """class that represent Books"""
    author=models.CharField(max_length=200,help_text='Enter the name of the author')
    TYPE_OF_EDITION=[
        ('PO','Poche 11 cm x 18 cm'),
        ('DG','Digest 14 cm x 21.6 cm'),
        ('RO','Roman 15 cm x 21 cm'),
        ('RY','Royal 16 cm x 24 cm'),
        ('A4','A4 21 cm x 29,7 cm'),
        ('AU','Autre')
        
    ]
    edition=models.CharField(max_length=2,help_text='veuillez selectionner le type d\'édition dans la liste déroulante', choices=TYPE_OF_EDITION, null=True, blank=True)
    TYPE_OF_BOOK=[
        ("RM","Roman"),
        ('BG','Biographie'),
        ('AB','Autobiographie'),
        ("MG","Manga"),
        ("ES","Essai"),
        ("BD","Bande Dessinée"),
        ("CS","Comics"),
        ("BL","Beau Livre"),
        ("AU","Autre"),
    ]
    type=models.CharField(max_length=2,choices=TYPE_OF_BOOK,help_text="choose the type of book")
    editeur=models.CharField(max_length=200,help_text='veuillez saisir le nom de l\'éditeur',blank=True, null=True)
    
class Watch (CollectionObject):
    """class that represents watches"""
    brand=models.CharField(max_length=100,help_text='enter the brand of your watch')
    Material=models.CharField(max_length=200,help_text='Enter the material(s) of your watch',blank=True, null=True)
    TYPE_OF_MECANISM=[
        ('MM','Mécanique manuel'),
        ('MA','Mécanique automatique'),
        ('QZ','Quartz (pile)'),
    ]
    type_of_mecanism=models.CharField(max_length=2, help_text='Enter the type of mecanism of your watch, e.g. automatic',blank=True, null=True, choices=TYPE_OF_MECANISM)
        
    
class Category(models.Model):
    """class that represent a category for a collection"""
    name=models.CharField(max_length=200,help_text='Enter the name of your category',unique=True)
    
    def __str__(self):
        return self.name
    
class Collection(models.Model):
    """class that represent a collection of objects"""
    name=models.CharField(max_length=200,help_text='Enter a name for your collection')
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    collection_objects=models.ManyToManyField('CollectionObject',help_text='Objects in this collection' )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """function required to display the detail of a collection"""
        return reverse('collection-detail',args=[str(self.id)])
    