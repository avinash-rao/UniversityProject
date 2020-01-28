from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'testapp/index.html')

def one(request):
    return render(request, 'testapp/one.html')
