from django.urls import path, include
from .views import UserAPIView, UserDetailAPIView, DepartamentAPIView, ProfileAPIView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'profile', ProfileAPIView, basename='profile_api')

urlpatterns =[
    path('api/staff/', UserAPIView.as_view()),
    path('api/staff/<int:pk>', UserDetailAPIView.as_view()),
    path('api/company/', DepartamentAPIView.as_view()),
    # path('api/users/<user_id>/profile/', ProfileAPIView.as_view()),
    path(r'api/', include(router.urls)),

    # path('api/profile/', ProfileAPIView.as_view()),
    # path('api/profile/<int:pk>', ProfileAPIView.as_view()),
]

