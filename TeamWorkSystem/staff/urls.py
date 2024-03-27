from django.urls import path
from .views import UserAPIView


urlpatterns =[
    path('api/staff/', UserAPIView.as_view()),
]