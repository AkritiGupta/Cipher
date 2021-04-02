from django.contrib.sites import requests
from django.shortcuts import render

# Create your views here


def home(request):
    return render(request, "home.html", {'name': "gen"})


def display(request):
    college_name = request.GET["college"]
    domain = request.GET["domain"]
    date = request.GET["date"]
    mode_of_payment = request.GET["amt"]
    trainer = request.GET["trainer"]
    no_of_days = request.GET["No_of_days"]
    mode_of_training = request.GET["training"]
    di = college_name + "" + domain + " " + date + " " + mode_of_payment + " " + trainer + " " + no_of_days + " " + mode_of_training
    return render(request, "home.html", {"d": di})
