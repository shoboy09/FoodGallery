from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def reservation(request):
    return render(request, 'base/reservation.html')

def contact(request):
    return render(request, 'base/contact.html')

def menu(request):
    return render(request, 'base/menu.html')