from django.shortcuts import render
from .models import Collection, CollectionObject,Category,Book,Watch
from django.http import JsonResponse
from django.views import generic

# Create your views here.
def index(request):
    return render(request,'index.html')

def get_collections_data(request):
    collections=Collection.objects.all()
    catalog_data=[]
    
    for collection in collections:
        collection_data={
            'id':str(collection.id),
            'name':collection.name,
            'category':collection.category.name,
            'collection_object':[]
            
        }
        for collection_object in collection.collection_objects.all():
            object_data={
                'object_id':str(collection_object.id),
                'object_name':collection_object.name,
                'object_description':collection_object.description,
                'object_image':str(collection_object.image.url) if collection_object.image else None,
            }
            collection_data['collection_object'].append(object_data)
        catalog_data.append(collection_data)
    
    
    
    context={
        'collections':catalog_data,
    }
    return JsonResponse(context)
    
class CollectionDetailView(generic.DetailView):
    model=Collection