from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from donations.models import Donation
from donations.serializers import DonationSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_donations_list(request):
    donations = Donation.objects.filter(user=request.user)
    serialized_donations = DonationSerializer(donations, many=True)
    return Response(serialized_donations.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_donation_by_id(request, id):
    donation = get_object_or_404(Donation, id=id)
    serialized_donation = DonationSerializer(donation)
    return Response(serialized_donation.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_create_donation(request):
    updated_request = request.data.copy()
    updated_request.update({'user': request.user.id})
    serialized_donation = DonationSerializer(data=updated_request)
    if serialized_donation.is_valid():
        serialized_donation.save()
        return Response(serialized_donation.data, status=status.HTTP_201_CREATED)
    return Response(serialized_donation.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_update_donation(request, id):
    donation = get_object_or_404(Donation, id=id)
    serialized_donation = DonationSerializer(instance=donation, data=request.data)
    if serialized_donation.is_valid():
        serialized_donation.save()
        return Response(serialized_donation.data, status=status.HTTP_200_OK)
    return Response(serialized_donation.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_donation(request, id):
    donation = get_object_or_404(Donation, id=id)
    donation.delete()
    return Response('Donation deleted', status=status.HTTP_200_OK)
