from rest_framework import serializers
from .models import CorporationNews, NewsComments

class NewsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')
    # далее заменить на ссылку или удалить оставив ID

    class Meta: 
        model = CorporationNews
        fields = ['title', 'text', 'publish', 'author', 'id']

# class NewsCreateSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = CorporationNews
#         fields = ['title', 'text']

class CommmentSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source = 'writer.username')
    # далее заменить на ссылку или удалить оставив ID

    class Meta:
        model = NewsComments
        fields = ['news', 'comment', 'date', 'writer', 'id']

class NewsDetailSerializer(serializers.ModelSerializer):
    Comments = CommmentSerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source = 'author.username')
    # далее заменить на ссылку или удалить оставив ID

    class Meta: 
        model = CorporationNews
        fields = ['title', 'text', 'publish', 'author', 'id', 'Comments']