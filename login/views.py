from django.contrib.auth.models import User
from login.serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ValidationError

from django.contrib.auth.hashers import check_password


class LoginViewSet(GenericViewSet):

    def retrieve(self, request, format=None):
        """Access login page"""
        return Response(status=status.HTTP_200_OK)

    def create(self, request, format=None):
        """Validate if user is authenticated."""
        serializer = LoginSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            user = User.objects.get(username=serializer.data["username"])

            if check_password(serializer.data["password"], user.password):
                return Response("User is authenticated! :)", status=status.HTTP_200_OK)
            else:
                return Response("User matching query does not exist.", status=status.HTTP_401_UNAUTHORIZED)
        except ValidationError as ex:
            return Response(ex.args[0], status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(ex.args[0], status=status.HTTP_401_UNAUTHORIZED)


class SignUpViewSet(GenericViewSet):
    pass

    # def post(self, request, format=None):
    #     """_summary_"""
    #     serializer = LoginSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(status=status.HTTP_201_CREATED)
