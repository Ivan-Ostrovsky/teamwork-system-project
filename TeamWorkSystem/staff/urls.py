from django.urls import path
from .views import UserAPIView, UserDetailAPIView, DepartamentAPIView


urlpatterns =[
    path('api/staff/', UserAPIView.as_view()),
    path('api/staff/<int:pk>', UserDetailAPIView.as_view()),
    path ('api/company/', DepartamentAPIView.as_view())
]