from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'profile_picture')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.password = make_password(validated_data['password'])
        user.is_active = False
        user.save()
        return user

