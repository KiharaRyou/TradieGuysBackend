from rest_framework import serializers
from coupons.models import Coupon

class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = ['id', 'parent', 'image', 'title', 'price', 'description', 'is_active', 'last_modified']