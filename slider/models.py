from django.db import models
#thumbnail
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail



# Create your models here.
class Slider(models.Model):
     title = models.CharField(max_length=300,default='',verbose_name='عنوان')
     description = models.TextField(default='',verbose_name='توضیحات')
     url = models.URLField(max_length=300,default='',verbose_name='آدرس لینک')
     url_title = models.CharField(max_length=300,default='',verbose_name='عنوان لینک')
     display_order = models.IntegerField(default=1,verbose_name='اولویت نمایش')
     image = models.ImageField(max_length=300,upload_to='images/sliders',default='',verbose_name='تصویر')

     def __str__(self):
          return self.title


     #for show image in list box
     def image_box(self):
          im = get_thumbnail(self.image, '100x100', crop='center', quality=99)
          return  mark_safe(f'<img src="{im.url}" />')

     class Meta:
          verbose_name = 'اسلایدر'
          verbose_name_plural = 'اسلایدرها'