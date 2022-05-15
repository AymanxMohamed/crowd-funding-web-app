from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes

from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.password = make_password(validated_data['password'])
        user.is_active = False
        user.save()
        return user

    def update(self, user, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        for attr, value in validated_data.items():
            setattr(user, attr, value)
        if 'password' in validated_data:
            user.password = make_password(validated_data['password'])

        user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'profile_picture', 'birth_date', 'facebook_link', 'country')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4}}


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
