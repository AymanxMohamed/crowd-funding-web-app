from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes

from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()


    def get_picture(self,obj):
        return obj.profile_picture.__str__().split("/")[-1]

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.password = make_password(validated_data['password'])
        user.is_active = False
        user.save()
        return user

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

    class Meta:
        model = User
        fields = ('id',  'first_name', 'last_name', 'email', 'phone_number', 'picture')
