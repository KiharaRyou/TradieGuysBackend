import os
from django.db import models
from django.utils import timezone

def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"images/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

class Image(models.Model):
    image = models.ImageField(upload_to=upload_to)