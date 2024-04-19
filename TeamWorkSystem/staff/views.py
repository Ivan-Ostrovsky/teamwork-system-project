from rest_framework import filters
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import User, UserDepartament
from .serializer import UserSerializer, UserDetailSerializer, DepartamentSerializer

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
# страничка отдельного пользовтеля + (в разработке) профиль
    
class DepartamentAPIView(generics.ListAPIView):
    queryset = UserDepartament.objects.all()
    serializer_class = DepartamentSerializer
# лист всей комапанни (без сокращения) разбитый по департаментам

# Create your views here.
