from dataclasses import fields
from rest_framework import serializers

from projects.models import Project, Image
from comments.models import Comment
from tags.models import Tag
from users.models import User
from categories.models import Category



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
        
#General Serializer for home page listing
class ProjectSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True, read_only=True,source='image_set')
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'details',
            'total_target',
            'start_date',
            'end_date',
            'is_featured',
            'images',
                  ]
        
class DetailedProjectSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True, read_only=True,source='image_set')
    comments = serializers.StringRelatedField(many=True, read_only=True,source='comment_set')
    # tags = serializers.StringRelatedField(many=True, read_only=True,source='tag_set')
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'details',
            'total_target',
            'start_date',
            'end_date',
            'is_featured',
            'images',
            'comments',
            'tags',
                  ]