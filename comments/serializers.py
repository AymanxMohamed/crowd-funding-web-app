from rest_framework import serializers

from comments.models import Comment
from projects.models import Project

class CommentSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    class Meta:
        model = Comment
        fields = "__all__"
        # read_only_fields = ('created_at', 'updated_at')
        # depth = 1
