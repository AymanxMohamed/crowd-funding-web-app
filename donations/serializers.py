from rest_framework import serializers

from .models import Donation


class DonationSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField('get_author_name')
    author_picture = serializers.SerializerMethodField('get_author_picture')

    class Meta:
        model = Donation
        fields = "__all__"

    def get_author_name(self, comment):
        return comment.user.first_name + " " + comment.user.last_name

    def get_author_picture(self, comment):
        return comment.user.profile_picture.__str__() or None