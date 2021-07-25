from rest_framework import serializers
from articles.models import Article, Comment
from users.serializers import UserSerializer

class ArticleSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'parent', 'title', 'content', 'created', 'is_active', 'owner', 'last_modified']

class CommentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'parent', 'content', 'created', 'is_active', 'owner', 'last_modified']