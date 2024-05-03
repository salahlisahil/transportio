from ckeditor.fields import RichTextField
from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    content = RichTextField()
    benefits = models.CharField(max_length=500)
    icon = models.ImageField(upload_to='services/')
    image = models.ImageField(upload_to='services/')
    video = models.URLField()
    video_banner = models.ImageField(upload_to='services/')

    def __str__(self):
        return f'<Service {self.title}>'


class WareHouse(models.Model):
    location = models.CharField(max_length=255)
    contact_number = models.BigIntegerField()
