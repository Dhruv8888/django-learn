from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def school_fees(request):
    return HttpResponse('100')
