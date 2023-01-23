from django.contrib.auth.models import User
from login.serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate, login


class LoginViewSet(GenericViewSet):
    serializer_class = LoginSerializer

    def retrieve(self, request, format=None):
        """Access login page"""
        return Response(status=status.HTTP_200_OK)

    def create(self, request, format=None):
        """Validate if user is authenticated."""
        username = request.data["auth"]["username"]
        password = request.data["auth"]["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response("User is authenticated! :)", status=status.HTTP_200_OK)
        else:
            return Response("User matching query does not exist.", status=status.HTTP_401_UNAUTHORIZED)


class SignUpViewSet(GenericViewSet):
    pass

    # def post(self, request, format=None):
    #     """_summary_"""
    #     serializer = LoginSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(status=status.HTTP_201_CREATED)
