from django.db import models
from categories.models import Category


class Coupon(models.Model):
    parent = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    last_modified = models.DateTimeField(auto_now=True, null=True)
    title = models.CharField(max_length=128)
    image = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super(Coupon, self).save(*args, **kwargs)
