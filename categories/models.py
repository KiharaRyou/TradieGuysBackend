from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=128, unique=True)
    is_active = models.BooleanField(default=False)

    @property
    def coupons(self):
        return len(self.coupon_set.all())

    @property
    def ads(self):
        return len(self.ad.all())

    @property
    def articles(self):
        return len(self.article_set.all())