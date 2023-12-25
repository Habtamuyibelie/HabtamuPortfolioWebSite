from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')
def certeficate(request):
    return render(request,'certeficate.html')

def about(request):
    return render(request,'about.html')
def comingsoon(request):
    return render(request,'comingsoon.html')
def skills(request):
    return render(request,'skills.html')