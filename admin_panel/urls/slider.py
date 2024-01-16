from django.urls import path
from ..views import slider

urlpatterns = [
    path('', slider.sliders_list ,name='sliders_list_view')
]