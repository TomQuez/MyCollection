from django.contrib import admin
from CollectionCatalog.models import  Collection, Category,Book, Watch, CollectionObject
# Register your models here.
admin.site.register(Collection)
admin.site.register(Category)
admin.site.register(CollectionObject)

admin.site.register(Book)
admin.site.register(Watch)

