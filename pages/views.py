from django.shortcuts import render

def home(request):
    return render(request,'pages/home.html')
# Create your views here.

def about(request):
    return render(request,'pages/about.html')

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')
