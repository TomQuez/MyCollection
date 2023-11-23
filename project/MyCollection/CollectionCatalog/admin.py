from django.contrib import admin
from CollectionCatalog.models import  Collection, Category,Book, Watch, CollectionObject
# Register your models here.

class CollectionAdmin(admin.ModelAdmin):
    list_display=('owner','name','category')
    list_filter=('owner','category','name')
   

class CollectionObjectAdmin(admin.ModelAdmin):
    list_display=('name','id')
    

  

class BookAdmin(admin.ModelAdmin):
    list_display=('name','author','type','edition','editeur')
    list_filter=('name','type','edition')
    fieldsets=(
        (None,{
            'fields':('name','author')
        }),
        ('Détails de l\'édition',{
            'fields':('type','edition','editeur')
        })
    )

class WatchAdmin(admin.ModelAdmin):
    list_display=('name','brand','type_of_mecanism')
    list_filter=('name','brand','type_of_mecanism')

admin.site.register(Collection,CollectionAdmin)
admin.site.register(Category)
admin.site.register(CollectionObject,CollectionObjectAdmin)

admin.site.register(Book,BookAdmin)
admin.site.register(Watch,WatchAdmin)

