from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import ratings

from ratings.serializers import RatingSerializer
from ratings.models import Rating

@api_view(['GET'])
def api_ratings_list(request):
    ratings = Rating.objects.all()
    serialized_ratings = RatingSerializer(ratings, many=True)
    return Response(serialized_ratings.data)

@api_view(['POST'])
def api_create_rating(request):
    serialized_rating = RatingSerializer(data=request.data)
    if serialized_rating.is_valid():
        serialized_rating.save()
        return Response(serialized_rating.data, status=status.HTTP_201_CREATED)
    return Response(serialized_rating.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_get_rating_by_id(request, pk):
    rating = get_object_or_404(Rating, id=pk)
    serialized_rating = RatingSerializer(rating)
    return Response(serialized_rating.data, status=status.HTTP_200_OK)
    
    
@api_view(['PUT'])
def api_update_rating(request, pk):
    rating = get_object_or_404(Rating, id=pk)
    serialized_rating = RatingSerializer(instance=rating, data=request.data)
    if serialized_rating.is_valid():
        serialized_rating.save()
        return Response(serialized_rating.data, status=status.HTTP_200_OK)
    return Response(serialized_rating.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def api_delete_rating(request, pk):
    rating = get_object_or_404(Rating, id=pk)
    rating.delete()
    return Response('success',status=status.HTTP_200_OK)
    