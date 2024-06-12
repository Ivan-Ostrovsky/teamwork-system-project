from django.urls import path, include
from .views import ProfileAPIView, ProfileShortAPIView, DepartamentAPIView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'profile', ProfileAPIView, basename='profile_api')
router.register(r'profile-short', ProfileShortAPIView, basename='profile_shortcut_api')

urlpatterns =[
    path(r'', include(router.urls)),
    path('company/', DepartamentAPIView.as_view()),
]

