from categories.models import Category
from articles.models import Article, Comment
from articles.serializer import ArticleSerializer, CommentSerializer
from rest_framework import generics, permissions, serializers
from utils.permissions import IsOwnerOrReadOnly
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class ListCreateArticle(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request):
        queryset = Article.objects.filter(owner=request.user)
        serializer = ArticleSerializer(queryset, many=True)
        return JsonResponse({
            'status': 'OK',
            'results': serializer.data
        })

    def post(self, request):
        catergory = Category.objects.get(id=request.data['category'])
        article = Article.objects.create(
            parent=catergory,
            owner=request.user, 
            title=request.data['title'],
            content=request.data['content']
        )
        serializer =  ArticleSerializer(article)
        return JsonResponse({
            'status': 'OK',
            'result': serializer.data
        })



class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

@api_view(['GET'])
def get_articles(request):
    category = request.GET.get('category', '')
    queryset = Article.objects.filter(is_active=True)
    serializer = ArticleSerializer(queryset, many=True)

    return JsonResponse({
        'status': 'OK',
        'results': serializer.data
    })