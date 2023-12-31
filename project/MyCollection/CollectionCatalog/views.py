from django.shortcuts import render, get_object_or_404
from .models import Collection, CollectionObject,Category,Book,Watch
from django.http import JsonResponse
from django.views import generic
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    num_visits=request.session.get('num_visits',1)
    request.session['num_visits']=num_visits+1 
    context={
        'num_visits':num_visits
    }
    return render(request,'index.html',context=context)

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
@login_required
def collection_details(request):
    collection_id=request.GET.get('id')
    context={'collection_id':collection_id}
    return render(request,'collection_detail.html',context)
    
def get_collection_details(request,id):
    collection=get_object_or_404(Collection,id=id)
    data={
        'name':collection.name,
        'category':collection.category.name,
        'collection_objects':[
            {'name':obj.name,'description':obj.description, 'image':obj.image.url if obj.image else None,} for obj in collection.collection_objects.all()
        ]
    }
    
    return JsonResponse(data)
@login_required
def user_collections(request):
    user_collections=Collection.objects.filter(owner=request.user)
    context={
        'user_collections':user_collections,
    }
    
    return render(request,'user_collection.html',context)