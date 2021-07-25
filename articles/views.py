from categories.models import Category
from articles.models import Article, Comment
from articles.serializer import ArticleSerializer, CommentSerializer
from rest_framework import generics, permissions, serializers
from utils.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status

class ListCreateArticle(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request):
        queryset = Article.objects.filter(owner=request.user)
        serializer = ArticleSerializer(queryset, many=True)
        return Response({
            'status': 'OK',
            'results': serializer.data
        })

    def post(self, request):
        catergory = Category.objects.get(id=request.data['parent'])
        article = Article.objects.create(
            parent=catergory,
            owner=request.user, 
            title=request.data['title'],
            content=request.data['content']
        )
        serializer =  ArticleSerializer(article)
        return Response({
            'status': 'OK',
            'result': serializer.data
        })
    
    def put(self, request):
        id = request.GET.get('id', '')
        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ArticleSerializer(article, data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

@api_view(['GET'])
def get_articles(request):
    categroies = request.GET.get('category', '')
    
    if categroies == '':
        queryset = Article.objects.all().order_by('-created')
    else:
        array = categroies.split(',')
        queryset = Article.objects.filter(parent__in=array).order_by('-created')
    serializer = ArticleSerializer(queryset, many=True)

    return Response({
        'status': 'OK',
        'results': serializer.data
    })

@api_view(['GET', 'POST'])
def comments(request):
    article_id = request.GET.get('id', '')
    if request.method == 'GET':
        comments = Comment.objects.filter(parent=article_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        article = Article.objects.get(id=article_id)
        comment = Comment.objects.create(owner=request.user, parent=article, content=request.data['content'])
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)