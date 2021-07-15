from categories.models import Category
from categories.serializers import CategorySerializer
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

@api_view(['GET'])
def get_active_categories(request):
    queryset = Category.objects.filter(is_active=True)
    serializer = CategorySerializer(queryset, many=True)

    return Response({
        'status': 'OK',
        'results': serializer.data
    })
