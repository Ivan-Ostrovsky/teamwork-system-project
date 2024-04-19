from rest_framework import serializers
from .models import CorporationNews, NewsComments

class NewsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')
    # далее заменить на ссылку или ID - удалять нельза сериализация при POST запросе

    class Meta: 
        model = CorporationNews
        fields = ['title', 'text', 'publish', 'author', 'id']

class CommmentSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source = 'writer.id')
    # далее заменить на ссылку или ID - удалять нельзя сериализация при POST запросе

    class Meta:
        model = NewsComments
        fields = ['comment', 'date', 'writer', 'id']