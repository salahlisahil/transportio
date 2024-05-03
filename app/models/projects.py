from ckeditor.fields import RichTextField
from django.db import models
from datetime import date


class ProjectImage(models.Model):
    image = models.ImageField(upload_to='projects/')

    # title = models.CharField(max_length=255)

    def __str__(self):
        return self.image.url


class ProjectInfo(models.Model):
    cl_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=255)
    tags = models.CharField(max_length=500)

    project_challenge = RichTextField()
    how_it_works = RichTextField()
    project_result = RichTextField()


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    title_tags = models.CharField(max_length=500)
    benefits = models.CharField(max_length=500)
    content = RichTextField()
    images = models.ManyToManyField(ProjectImage, related_name='projects', blank=True)
    icon = models.ImageField(upload_to='services/')
    video = models.URLField()
    video_banner = models.ImageField(upload_to='services/')
    info = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Project {self.title}>'