from coupons.models import Coupon
from orders.models import Order, OrderItem
from orders.serializer import OrderSerializer
from rest_framework import generics, permissions, serializers
from utils.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

class ListCreateOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = Order.objects.filter(owner=request.user)
        serializer = OrderSerializer(queryset, many=True)
        return Response({
            'status': 'OK',
            'results': serializer.data
        })

    def post(self, request):
        order = Order.objects.create(owner=request.user, payment=request.data['payment'])
        for item in request.data['items']:
            coupon = Coupon.objects.get(id=item['coupon'])
            OrderItem.objects.create(order=order, coupon=coupon, price=item['price'])

        return Response({
            'status': 'OK',
        })



class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
