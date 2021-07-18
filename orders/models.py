from django.db import models
from coupons.models import Coupon
from users.models import User

class Order(models.Model):
    class PaymentMethod(models.IntegerChoices):
        PayPal = 1
        Master = 2
        Visa = 3

    owner = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    payment = models.IntegerField(choices=PaymentMethod.choices, null=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def amount(self):
        result = 0
        items = OrderItem.objects.filter(order=self)
        for item in items:
            result += item.price
        return result

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