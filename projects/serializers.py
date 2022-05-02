from rest_framework import serializers

from projects.models import Project, Image
from donations.serializers import DonationSerializer
from tags.serializers import TagsSerializer
from comments.serializers import CommentSerializer
from categories.serializers import CategorySerializer
from users.serializers import UserSerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']
        # fields = '__all__'


# General Serializer for home page listing
class ProjectSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True, read_only=True, source='image_set')
    donations = DonationSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
        include_fields = ('images', 'donations')


class DetailedProjectSerializer(serializers.ModelSerializer):
    donation = DonationSerializer(many=True, read_only=True)
    tags = TagsSerializer(many=True)
    images = ImageSerializer(many=True, source='image_set')
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    category = CategorySerializer(many=False, read_only=True)
    donations = DonationSerializer(many=True, read_only=True, source='donation_set')
    owner = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
