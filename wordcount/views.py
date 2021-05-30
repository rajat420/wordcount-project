from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')

def eggs(request):
    return HttpResponse('Eggs are great!')

def resume(request):
    return render(request,'resume.html')

def index(request):
    return render(request,'index.html')
