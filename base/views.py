from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


courses = [
      'Python',
      'Django',
      'JavaScript',
      'ASP net Core',
      'C#',
      'Angular'
]

# Home Page Action
def home_view(request: HttpRequest):
      return render(request,'base/index.html')

# About Us Page Action
def about_view(request: HttpRequest):
      """ Context = db"""
      context = {
            'courses': courses
      }
      return render(request,'base/about.html',context)