from django.db import models
from coupons.models import Coupon
from users.models import User

class Order(models.Model):
    owner = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    payment = models.DecimalField(max_digits=1, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created

    class Meta:
        ordering = ['created']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, related_name='order_items', on_delete=models.CASCADE)
    price= models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.id