from django.urls import path
from course import views

urlpatterns = [
    path('learndj/', views.learndj),
    path('stdata/', views.stdata),
    path('registration/', views.showformdata),

]