from django.db import models

class Category(models.Model):
    image = models.CharField(max_length=128, null=True)
    title = models.CharField(max_length=128, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title