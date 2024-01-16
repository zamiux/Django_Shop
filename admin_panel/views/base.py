from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from slider.models import Slider


def dashboard(request: HttpRequest):
    context = { 'page_title': 'داشبورد ادمین' }
    return render(request,'admin_panel/base/base.html',context)
