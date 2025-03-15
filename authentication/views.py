from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homePage(request):
    return render(request , "homePage.html")

def signup(request):
    return render(request , "authentication/signup.html")

def login(request):
    return render(request , "authentication/login.html")

def logout(request):
    pass