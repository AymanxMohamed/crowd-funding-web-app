from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from tags.models import Tag
from tags.serializers import TagsSerializer
from projects.models import Project
from projects.serializers import ProjectSerializer

@api_view(['GET'])
def api_tags_list(request):
    tags = Tag.objects.all()
    serialized_tags = TagsSerializer(tags, many=True)
    return Response(serialized_tags.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def api_get_tag_by_id(request, id):
    tag = get_object_or_404(Tag, id=id)
    serialized_tag = TagsSerializer(tag)
    return Response(serialized_tag.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def api_get_related_projects_by_tag(request, id):
    projects = Project.objects.filter(tags__id=id)
    serialized_projects = ProjectSerializer(projects, many=True)
    return Response(serialized_projects.data, status=status.HTTP_200_OK)
    

@api_view(['POST'])
def api_create_tag(request):
    serialized_tag = TagsSerializer(data=request.data)
    if serialized_tag.is_valid():
        serialized_tag.save()
        return Response(serialized_tag.data, status=status.HTTP_201_CREATED)
    return Response(serialized_tag.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def api_update_tag(request, id):
    tag = get_object_or_404(Tag, id=id)
    serialized_tag = TagsSerializer(instance=tag, data=request.data)
    if serialized_tag.is_valid():
        serialized_tag.save()
        return Response(serialized_tag.data, status=status.HTTP_200_OK)
    return Response(serialized_tag.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delete_tag(request, id):
    tag = get_object_or_404(Tag, id=id)
    tag.delete()
    return Response('Tag deleted', status=status.HTTP_200_OK)