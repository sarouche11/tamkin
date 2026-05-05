from django.urls import path
from . import views

urlpatterns = [

    path('get-data/<str:nin>', views.get_miclate_data, name='get_data'),


]



    
