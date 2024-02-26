from django.contrib.auth import authenticate
from django.contrib.auth.base_user import password_validation
from rest_framework.authtoken.models import Token
from rest_framework import serializers

from users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'company'
        )


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def validate(self, data):
        user = authenticate(
            username=data['username'], password=data['password'])

        if not user:
            raise serializers.ValidationError('Credenciales no validas')

        self.context['user'] = user
        return data

    def create(self, data):
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class UserSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    is_staff = serializers.BooleanField()

    password = serializers.CharField(min_length=8, max_length=128)
    password_confirmation = serializers.CharField(min_length=8, max_length=128)

    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']

        if passwd != passwd_conf:
            raise serializers.ValidationError("Contraseñas no coinciden")

        password_validation.validate_password(passwd)

        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        return user
