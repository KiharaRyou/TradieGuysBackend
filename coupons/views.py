from coupons.models import Coupon
from coupons.serializers import CouponSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CouponList(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

class CouponDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

class CouponDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

@api_view(['GET'])
def get_active_coupons(request):
    queryset = Coupon.objects.filter(is_active=True)
    serializer = CouponSerializer(queryset, many=True)

    return Response({
        'status': 'OK',
        'results': serializer.data
    })

@api_view(['GET'])
def get_similar_coupons(request):
    id = request.GET.get('id', '')
    parent = request.GET.get('parent', '')
    print(id)
    print(parent)
    queryset = Coupon.objects.filter(parent=parent).exclude(id=id)[:5]
    serializer = CouponSerializer(queryset, many=True)

    return Response({
        'status': 'OK',
        'results': serializer.data
    })
