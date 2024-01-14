from django.db import models

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



     class Meta:
          verbose_name = 'اسلایدر'
          verbose_name_plural = 'اسلایدرها'