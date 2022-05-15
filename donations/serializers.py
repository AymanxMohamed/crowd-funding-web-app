from rest_framework import serializers

from .models import Donation


class DonationSerializer(serializers.ModelSerializer):
    donor_name = serializers.SerializerMethodField()
    project_picture = serializers.SerializerMethodField()
    project_title = serializers.SerializerMethodField()

    class Meta:
        model = Donation
        fields = "__all__"

    def get_project_picture(self, comment):
        return comment.project.image_set.first().image.__str__()

    def get_project_title(self, comment):
        return comment.project.title

    def get_donor_name(self, comment):
        return comment.user.first_name + " " + comment.user.last_name
