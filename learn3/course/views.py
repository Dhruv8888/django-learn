from django.shortcuts import render
from course.models import Student
from .forms import StudentRegistration
# Create your views here.

def learndj(request):
    name='django'
    duration='5 months'
    fees=500
    info={'nm':name,'du':duration, 'fe':500 }
    return render(request, 'course/base.html',info )

def stdata(request):
    std=Student.objects.all()
    return render(request, 'course/stdata.html', {'stud':std})

def showformdata(request):
    fm=StudentRegistration()
    return render(request, 'enroll/userregistration.html',{'form':fm })