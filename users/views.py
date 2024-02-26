from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserLoginSerializer, UserModelSerializer, UserSignUpSerializer


class UserLogin_ViewSet(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)


class User_ViewSet(APIView):

    """
    TODO: 
        - Get list users
        - Put user
        - Deactivate user
    """

    def post(self, request, format=None):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
