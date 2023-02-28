from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=100)
    password = serializers.CharField(required=True, max_length=100)

class SignUpSerializer(LoginSerializer):
    confirm_password = serializers.CharField(required=True, max_length=100)
