from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from users.models import User
from articles.models import Article
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from users.serializers import RegisterSerializer, UserSerializer
from articles.serializer import ArticleSerializer



@api_view(['GET', 'POST'],)
def users_api(request):
    if request.method == 'GET':
        users = sorted(User.objects.all(), key=lambda t: t.article_count, reverse=True)[:4]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    if request.method == 'POST':    
        serializers = RegisterSerializer(data=request.data)
        data = {}

        if serializers.is_valid():
            user = serializers.save()
            data['status'] = 'OK'
            data['email'] = user.email
            data['username'] = user.username
        else:
            data['status'] = 'Error'
            data['reasons'] = serializers.errors

        return Response(data)

@api_view(['GET', 'PUT'])
def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        articles = Article.objects.filter(owner=user)
        article_serializer = ArticleSerializer(articles, many=True)
        return Response({
            'articles': article_serializer.data,
            **serializer.data
        })

    elif request.method == 'PUT':
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'OK',
                **serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(user)
            return Response({
                'status': 'OK',
                'token': token.key,
                **serializer.data
            })
        else:
            return Response({
                'status': 'Error',
                'reason': 'Account does not exist or password is not correct'
            })

@api_view(['GET'])
def get_current_user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response({
        **serializer.data
    })

@api_view(['GET'],)
def get_staff(request):
    if request.method == 'GET':
        users = User.objects.filter(is_admin=True)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)