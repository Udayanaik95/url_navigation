from django.shortcuts import render

# Create your views here.

def First(request):
    return render(request,'First.html')

def Second(request):
    return render(request,'Second.html')