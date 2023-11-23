from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('get_collections_data/',views.get_collections_data,name='get_collections_data'),
    # path('collection/<int:id>/',views.collection_detail,name='collection_detail'),
    path('get_collection_details/<int:id>/',views.get_collection_details,name='get-collection-details'),
    path('collection_details/',views.collection_details,name='collection_details'),
    path('user_collections/',views.user_collections,name="user_collections")
   
]