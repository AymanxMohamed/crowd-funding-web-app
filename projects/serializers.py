from rest_framework import serializers
from donations.models import Donation

from projects.models import Project, Image
from donations.serializers import DonationSerializer
from tags.serializers import TagsSerializer
from comments.serializers import CommentSerializer
from categories.serializers import CategorySerializer
from users.serializers import UserSerializer
from django.db.models import Sum, Avg


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image_name']
        # fields = '__all__'


# General Serializer for home page listing
class ProjectSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True, read_only=True, source='image_set')
    donations = DonationSerializer(many=True, read_only=True)
    total_donations = serializers.SerializerMethodField()
    average_ratings = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        return obj.category.name

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance

    def get_total_donations(self, obj):
        return obj.donation_set.aggregate(Sum('amount'))['amount__sum'] or 0
    
    def get_average_ratings(self, obj):
        return obj.rating_set.aggregate(Avg('rating'))['rating__avg'] or 0

    class Meta:
        model = Project
        fields = "__all__"


class DetailedProjectSerializer(serializers.ModelSerializer):
    # donation = DonationSerializer(many=True, read_only=True)
    tags = TagsSerializer(many=True)
    images = ImageSerializer(many=True, source='image_set')
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    category = CategorySerializer(many=False, read_only=True)
    donations = DonationSerializer(many=True, read_only=True, source='donation_set')
    owner = UserSerializer(many=False, read_only=True)
    total_donations = serializers.SerializerMethodField()
    average_ratings = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        return obj.category.name

    def get_total_donations(self, obj):
        return obj.donation_set.aggregate(Sum('amount'))['amount__sum'] or 0

    def get_average_ratings(self, obj):
        return obj.rating_set.aggregate(Avg('rating'))['rating__avg'] or 0
    class Meta:
        model = Project
        fields = "__all__"
