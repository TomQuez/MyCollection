from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('get_collections_data/',views.get_collections_data,name='get_collections_data')
]