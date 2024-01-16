from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    #pass
    list_display = ['image_box','__str__','title','url','url_title','display_order']
    list_editable = ['url','url_title']
    list_filter = ['title']
    search_fields = ['title','url','url_title']