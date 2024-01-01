from django.urls import path
# add Logic(view) to urls
from . import views

urlpatterns = [
    path('', views.home_view),
    path('about/', views.about_view)
]