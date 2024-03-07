from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns=[
    
    path('',views.home),
    path('show',views.show),
    path('send',views.send),
    path('delete',views.delete),
    path('edit',views.edit),
    path('RecordEdited',views.RecordEdited),
    path('search',views.search),
    path('searchid',views.searchid),   
]
