from rest_framework import filters
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import User, UserDepartament
from .serializer import UserSerializer, UserDetailSerializer, DepartamentSerializer
from .permission import IsAuthorOrReadOnly
from rest_framework.permissions import  IsAuthenticated
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'first_name', 'last_name', 'position']
# список всех пользователей = книга контактов

class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated  &  IsAuthorOrReadOnly]
# страничка отдельного пользовтеля + (в разработке) профиль

class DepartamentAPIView(generics.ListAPIView):
    queryset = UserDepartament.objects.all()
    serializer_class = DepartamentSerializer
# лист всей комапанни (без сокращения) разбитый по департаментам

# class ProfileAPIView(APIView):
#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)
# профиль get  - возможность просматреть

class ProfileAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "current":
            return self.request.user
        # профиль текущего пользователя

        return super().get_object()

# Create your views here.
