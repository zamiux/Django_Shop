from django import template
from slider import models

register = template.Library()

@register.inclusion_tag('sliders/slider_inclusions.html')
def sliders_list_inclusion(*args,**kwargs):
    # select * from slider_slider
    #sliders = models.Slider.objects.all()

    # select * from slider_slider order by display_order desc
    #sliders = models.Slider.objects.order_by('display_order',descending=True).all()
    sliders = models.Slider.objects.order_by('-display_order') #in - hamoon kare desc mikone

    # select * from slider_slider where title like '%one%' order by display_order desc
    #sliders = sliders.filter(title__icontains='one')

    return {
        'sliders': sliders
    }