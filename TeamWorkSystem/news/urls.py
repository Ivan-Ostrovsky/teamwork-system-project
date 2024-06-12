from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers 
from .views import NewsViewSet, CommentsViewSet


router = SimpleRouter()
router.register(r'news', NewsViewSet, basename='News')

news_router = routers.NestedSimpleRouter(router, r'news', lookup='news')
news_router.register(r'comments', CommentsViewSet, basename="Comments-News")


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(news_router.urls)),
]