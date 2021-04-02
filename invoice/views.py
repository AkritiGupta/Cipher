from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests, "home.html", {'name':"Keerthi"})
def display(requests):
    college=requests.GET["college"]
    domain=requests.GET["domain"]
    date = requests.GET["trip-start"]
    mode_pay = requests.GET["mode_of_payment"]
    trainer = requests.GET["trainer"]
    tot_hrs = requests.GET["No_of_days"]
    mode = requests.GET["mode_of_training"]
    result=college+" "+domain+" "+date+" "+mode_pay+" "+trainer+" "+tot_hrs+" "+mode
    return render(requests,"home.html",{'res':result})