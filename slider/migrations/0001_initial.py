# Generated by Django 5.0 on 2024-01-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=300)),
                ('description', models.TextField(default='')),
                ('url', models.URLField(default='', max_length=300)),
                ('url_title', models.CharField(default='', max_length=300)),
                ('display_order', models.IntegerField(default=1)),
            ],
        ),
    ]