from ckeditor.fields import RichTextField
from django.db import models
from datetime import datetime, date


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=255)
    date = models.DateField(default=date.today)
    tags = models.CharField(max_length=500)
    topic = models.CharField(max_length=255)

    content = RichTextField()
    image = models.ImageField(upload_to='blogs/')

    def __str__(self):
        return f'<Blog {self.title}>'


class Comment(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.today)
    subject = models.CharField(max_length=255)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'<Comment {self.fullname}>'