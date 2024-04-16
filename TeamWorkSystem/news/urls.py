from django.urls import path
from .views import NewsListAPIView, NewsDetailAPIView, NewsUpdateAPIView

urlpatterns = [
    path('api/news/', NewsListAPIView.as_view()),
    path('api/update-news/<int:pk>/', NewsUpdateAPIView.as_view()),
    path('api/news/<int:pk>/', NewsDetailAPIView.as_view()),
    # path('api/comments/', CommentList.as_view()),

]