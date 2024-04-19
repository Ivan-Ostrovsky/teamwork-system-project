from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import CorporationNews, NewsComments
from .serializer import NewsSerializer, CommmentSerializer

class NewsListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50
# пагинатор класс    

class NewsListAPIView(generics.ListCreateAPIView):
    queryset = CorporationNews.objects.all()
    serializer_class = NewsSerializer
    #  permission_classes послде настроек разрешения
    pagination_class = NewsListPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
# Список новостей компании

class NewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CorporationNews.objects.all()
    serializer_class = NewsSerializer
    #  permission_classes послде настроек разрешения
# страница новости с возможность редактирования и удаления

class CommmentsListAPIView(generics.ListCreateAPIView):
    serializer_class = CommmentSerializer

    def get_queryset(self):
        return NewsComments.objects.filter(news=self.kwargs['news_id'])
    
    # def get_queryset(self):
    #     return CorporationNews.objects.get(pk=self.kwargs['news_id']).Comments.all()
    # альтернативный вариант - обращение черз модель "Новости"

    def perform_create(self, serializer):
        serializer.save(
            writer=self.request.user,
            news_id=self.kwargs['news_id']
            )
    # сохраням коменттора и ID новости
# Лист коментарии к конкретной новости по ID

class CommmentsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = NewsComments.objects.all()
    serializer_class = CommmentSerializer
    #  permission_classes послде настроек разрешения

    def get_queryset(self):
        return NewsComments.objects.filter(news=self.kwargs['news_id'])
    
    def perform_create(self, serializer):
        serializer.save(
            writer=self.request.user,
            news_id=self.kwargs['news_id']
            )
    # сохраням коменттора и ID новости
# страница коментария с возможность редактирования и удаления       


# Create your views here.
