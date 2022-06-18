from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(trim_whitespace=False, style={'input_type': 'password'})

    def validate_password(self, value):
        if not validate_password(value):
            return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'created_at', 'modified_at', 'date_joined']
