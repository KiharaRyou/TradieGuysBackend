from rest_framework import serializers
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'amount', 'payment', 'items', 'created']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order', 'coupon', 'price']