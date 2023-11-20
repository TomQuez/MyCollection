from django.contrib import admin
from CollectionCatalog.models import  Collection, Category,Book, Watch, CollectionObject
# Register your models here.
class CollectionAdmin(admin.ModelAdmin):
    list_display=('name','category')
    list_filter=('category','name')

class CollectionObjectAdmin(admin.ModelAdmin):
    list_display=('name','id')

class BookAdmin(admin.ModelAdmin):
    list_display=('name','author','type','edition')
    list_filter=('name','type','edition')

class WatchAdmin(admin.ModelAdmin):
    list_display=('name','brand','type_of_mecanism')
    list_filter=('name','brand','type_of_mecanism')

admin.site.register(Collection,CollectionAdmin)
admin.site.register(Category)
admin.site.register(CollectionObject,CollectionObjectAdmin)

admin.site.register(Book,BookAdmin)
admin.site.register(Watch,WatchAdmin)

