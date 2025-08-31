from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def booking(request):
    return render(request, 'book.html')

def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')