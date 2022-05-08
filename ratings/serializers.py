from rest_framework import serializers
from ratings.models import Rating

from users.serializers import UserSerializer
from projects.serializers import ProjectSerializer
class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, required=False, allow_null=True)
    project = serializers.StringRelatedField(read_only=True, required=False, allow_null=True)
    class Meta:
        model = Rating
        fields = '__all__'