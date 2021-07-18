from rest_framework import serializers
from orders.models import Order, OrderItem

class OrderItemListingField(serializers.RelatedField):
    def to_representation(self, value):
        coupon = value.coupon
        return ({
            'id': coupon.id,
            'image': coupon.image,
            'title': coupon.title,
            'price': value.price
        })

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemListingField(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'items', 'amount', 'payment', 'created']