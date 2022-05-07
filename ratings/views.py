from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_ratings_list(request):
    pass

@api_view(['POST'])
def api_create_rating(request):
    pass

@api_view(['GET'])
def api_get_rating_by_id(request):
    pass

@api_view(['PUT'])
def api_update_rating(request):
    pass

@api_view(['DELETE'])
def api_delete_rating(request):
    pass