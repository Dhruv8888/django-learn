from django.urls import path
from course import views


urlpatterns = [
    
    
     
     path('learndj/', views.learn_django),
      
     path('home/', views.home),
]