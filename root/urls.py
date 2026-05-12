from django.urls import path
from .views import index,register, load_communes,forbidden,register_id,success,comming_soon


urlpatterns = [
    path('', index ,name='index'),
    path('register/', register ,name='register'),
    path('register_id/<str:code>', register_id ,name='register'),

    path('ajax/load-communes/', load_communes, name='ajax_load_communes'),
    path('forbidden/<int:code>/', forbidden, name='forbidden'),
    path('success/<str:code>/', success, name='success'),

    path('comming_soon/', comming_soon, name='comming_soon'),
  
]



    
