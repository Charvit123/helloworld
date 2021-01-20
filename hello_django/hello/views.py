from django.shortcuts import render
from django.http import HttpResponse
def djangoproject(request):
    return render(request,'hello.html')
# Create your views here.
