from orders.models import Order, OrderItem
from orders.serializer import OrderSerializer, OrderItemSerializer
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from utils.permissions import IsOwnerOrReadOnly

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):

        order = serializer.save(owner=self.request.user)
        for i in order.items:
            item = OrderItem.objects.create(order=order.id)

            

class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
