from rest_framework import serializers
from tags.models import Tag


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
