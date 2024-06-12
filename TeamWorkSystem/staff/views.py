
from rest_framework import generics, mixins, viewsets

from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .permission import IsAuthorOrReadOnly
from rest_framework.permissions import  IsAuthenticated

from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication


from .models import User, UserDepartament
from .serializer import UserSerializer, UserShortSerializer, DepartamentSerializer

class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]
# представление для входа по логину и паролю

class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50
# пагинатор

class UserShortPagination(PageNumberPagination):
    page_size = 50
# пагинатор для Shortcut

class ProfileAPIView(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated  &  IsAuthorOrReadOnly]
    pagination_class = UserPagination # пагинация
    filter_backends = [filters.SearchFilter] # поиск нужного сотрудникка (пользователя)
    search_fields = ['username', 'first_name', 'last_name', 'position'] # параметры поиска


    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "current":
            return self.request.user
        # профиль текущего пользователя

        return super().get_object()
# список всех пользователей + траничка отдельного пользовтеля +  профиль (с возможностью редактирования)
    
class ProfileShortAPIView(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserShortSerializer
    pagination_class = UserShortPagination
# список всех пользователей = книга контактов ( СоКращенная инфо о пользователе(ях))

class DepartamentAPIView(generics.ListAPIView):
    queryset = UserDepartament.objects.all()
    serializer_class = DepartamentSerializer
# лист всей комапанни (без сокращения) разбитый по департаментам

# Create your views here.
