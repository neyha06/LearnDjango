from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("You are at home")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("You are at about")

def contact(request):
    return HttpResponse("You are at contact")
