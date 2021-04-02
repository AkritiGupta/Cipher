from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests, "home.html", {'name':"Preethi"})
def display(request):
    name = request.GET["name"]
    domain = request.GET["domain"]
    result = name+"Welcome to training on"+ domain
    return render(request, "home.html", {"res":"result"})

