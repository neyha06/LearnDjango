from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("You are at home")
    return render(request,'website/index.html')

def about(request):
    # return HttpResponse("You are at about")
    return render(request,'website/about.html')

def contact(request):
     return render(request,'website/contact.html')