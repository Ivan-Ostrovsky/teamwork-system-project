from django.urls import path
from .views import NewsListAPIView, NewsDetailAPIView, CommmentsListAPIView, CommmentsDetailAPIView

urlpatterns = [
    path('api/news/', NewsListAPIView.as_view()),
    path('api/news/<int:pk>/', NewsDetailAPIView.as_view()),
    path('api/news/<news_id>/comments/', CommmentsListAPIView.as_view()),
    path('api/news/<news_id>/comments/<int:pk>/', CommmentsDetailAPIView.as_view()),
]