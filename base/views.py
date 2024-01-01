from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Home Page Action
def home_view(request: HttpRequest):
      return render(request,'base/index.html')

# About Us Page Action
def about_view(request: HttpRequest):
      return render(request,'base/about.html')