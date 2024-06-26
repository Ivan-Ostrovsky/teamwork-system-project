from rest_framework import serializers
from .models import User, UserDepartament

class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'position', 'user_pic' ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'department',
            'username',
            'first_name',
            'last_name',
            'date_of_birth',
            'email',
            'position',
            'user_pic',
            'info'
            ]
        read_only_fields = ['username'] # поле теолько для чтения


class DepartamentSerializer (serializers.ModelSerializer):
    worker = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
     )
    
    class Meta:
        model = UserDepartament
        fields = ['id', 'name', 'worker']