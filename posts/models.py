from django.db import models
import datetime
import os


def get_name_ext(filepath):
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)
    return name, ext


def upload_image_path(instance, filepath):
    name, ext = get_name_ext(filepath)
    path = f"posts/{instance.category}-{instance.id}{ext}"
    print(path)
    return path


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, default="cat")
    author = models.CharField(max_length=20, default="author")
    views = models.IntegerField(default=0)
    date_published = models.DateTimeField(default=datetime.datetime.now())
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True, max_length=200)
    description = models.TextField()