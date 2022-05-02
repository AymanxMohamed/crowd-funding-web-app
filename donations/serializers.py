from rest_framework import serializers

from .models import Donation


class DonationSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Donation
        fields = "__all__"
