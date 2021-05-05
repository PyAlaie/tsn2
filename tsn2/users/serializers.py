from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['email', 'fullname', 'password']
        extra_kwargs = {
            'fullname': {'required': True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            fullname=validated_data['fullname'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
