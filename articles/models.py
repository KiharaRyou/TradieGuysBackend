from django.db import models
from django.db.models.fields.files import ImageField
from categories.models import Category
from users.models import User


class Article(models.Model):
    parent = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    title = models.CharField(max_length=128)
    content = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class Comment(models.Model):
    parent = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['created']