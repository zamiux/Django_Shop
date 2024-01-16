from django.urls import path,include

urlpatterns = [
    path('', include('admin_panel.urls.base')),
    path('sliders/', include('admin_panel.urls.slider'))
]