from rest_framework import serializers

from comments.models import Comment
from projects.models import Project
from users.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    owner = UserSerializer(many=False, read_only=True)
    
    class Meta:
        model = Comment
        fields = "__all__"

