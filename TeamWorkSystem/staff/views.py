from rest_framework import generics
from .models import User, UserDepartament
from .serializer import UserSerializer, UserDetailSerializer, DepartamentSerializer

class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# список всех пользователей = книга контактов

class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
# страничка отдельного пользовтеля + (в разработке) профиль
    
class DepartamentAPIView(generics.ListAPIView):
    queryset = UserDepartament.objects.all()
    serializer_class = DepartamentSerializer

# Create your views here.
