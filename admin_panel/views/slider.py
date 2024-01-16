from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from slider import models as slider_models


def sliders_list(request: HttpRequest):
    #show one data from GET requested.
    #print(request.GET)

    # show all data from GET requested.
    #print(request.GET.getlist())

    #print(f'title: {request.GET.get("title")}')
    #print(f'url: {request.GET.get("url")}')

    #filter
    title = request.GET.get('title')
    url = request.GET.get('url')

    sliders = slider_models.Slider.objects.all()

    if title:
        sliders = sliders.filter(title__icontains=title)

    if url:
        sliders = sliders.filter(url__icontains=url)

    context = {
        'page_title': 'لیست اسلایدرها',
        'sliders': sliders
    }
    return render(request,'admin_panel/slider/sliders.html',context)
