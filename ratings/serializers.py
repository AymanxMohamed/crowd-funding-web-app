from rest_framework import serializers
from ratings.models import Rating
from users.models import User
from projects.models import Project

from users.serializers import UserSerializer
from projects.serializers import ProjectSerializer


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Rating
        fields = '__all__'
