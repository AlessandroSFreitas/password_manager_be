from django.contrib.auth.models import User
from login.serializers import LoginSerializer, SignUpSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import authenticate, login


class LoginViewSet(GenericViewSet):
    serializer_class = LoginSerializer

    # def retrieve(self, request, format=None):
    #     """Access login page"""
    #     return Response(status=status.HTTP_200_OK)

    def create(self, request, format=None):
        """Validate if user is authenticated."""
        username = request.data["auth"]["username"]
        password = request.data["auth"]["password"]
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response("User is authenticated! :)", status=status.HTTP_200_OK)
            else:
                return Response("User matching query does not exist.", status=status.HTTP_401_UNAUTHORIZED)
        except Exception as ex:
            return Response(ex.args, status=status.HTTP_400_BAD_REQUEST)


class SignUpViewSet(GenericViewSet):
    serializer_class = SignUpSerializer

    def create(self, request, format=None):
        """Create user on application."""
        username = request.data["username"]
        password = request.data["password"]
        confirm_password = request.data["confirm_password"]

        if not password == confirm_password:
            return Response("Password must to be equal to confirm password!", status=status.HTTP_406_NOT_ACCEPTABLE)

        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            User.objects.create_user(username=username, email="", password=password)
        except Exception as ex:
            return Response(ex.args, status=status.HTTP_400_BAD_REQUEST)

        return Response("User successfully created!", status=status.HTTP_201_CREATED)
