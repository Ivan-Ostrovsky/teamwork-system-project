from django.shortcuts import render
from rest_framework import generics
from .models import CorporationNews, NewsComments
from .serializer import NewsSerializer, NewsDetailSerializer

class NewsListAPIView(generics.ListCreateAPIView):
    queryset = CorporationNews.objects.all()
    serializer_class = NewsSerializer
    #  permission_classes послде настроек разрешения

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class NewsUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CorporationNews.objects.all()
    serializer_class = NewsSerializer
    #  permission_classes послде настроек разрешения

# class CommentList(generics.ListCreateAPIView):
#     queryset = NewsComments.objects.all()
#     serializer_class = CommmentSerializer
#     #  permission_classes послде настроек разрешения

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

class NewsDetailAPIView(generics.RetrieveAPIView):
    queryset = CorporationNews.objects.all()
    serializer_class = NewsDetailSerializer
    #  permission_classes послде настроек разрешения



# Create your views here.
