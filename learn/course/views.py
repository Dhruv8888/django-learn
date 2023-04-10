from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learn_django(request):
    name= 'django'
    duration= '10 months'
    fees= 500
    django_details= {'nm':name,'du':duration, 'fe':fees }
    return render(request, 'course/base.html', django_details)

def home(request):
    return render(request, 'course/base.html')
    
