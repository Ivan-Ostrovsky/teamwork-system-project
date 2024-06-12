from rest_framework import viewsets 
from rest_framework.pagination import PageNumberPagination
from .models import CorporationNews, NewsComments
from .serializer import NewsSerializer, CommmentSerializer
from .permission import IsAuthorOrReadOnly, IsWriterOrReadOnly
from rest_framework.permissions import  IsAuthenticated

class NewsListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50
# пагинатор класс    

class NewsViewSet(viewsets.ModelViewSet):
    queryset = CorporationNews.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated  &  IsAuthorOrReadOnly] # он поддерживает & (и), | (или) и ~ (не).
    # только автор может редактировать новость

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # ? добавить фунукцию на редактирование - не надо (сохраннеия автора) 
    # (при внесение правок тоже работает) - посмотреть документацию
    
# новости

class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommmentSerializer
    permission_classes = [IsAuthenticated  & IsWriterOrReadOnly]
    # только (автор комента) коментатор может редактировать коментарий

    def get_queryset(self):
        return NewsComments.objects.filter(news=self.kwargs['news_pk'])
    
    def perform_create(self, serializer):
        serializer.save(
            writer=self.request.user,
            news_id=self.kwargs['news_pk']
            )
    # сохраням коменттора и ID новости (при внесение правок тоже работает)
# коментарии к новостям   


# Create your views here.
