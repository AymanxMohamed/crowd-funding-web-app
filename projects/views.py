from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from projects.models import Project
from projects.serializers import ProjectSerializer, DetailedProjectSerializer


@api_view(['GET'])
def api_projects_list(request):
    projects = Project.objects.all()
    projects_serialized = ProjectSerializer(projects, many=True)
    return Response(projects_serialized.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_get_project_by_id(request, id):
    project = Project.objects.get(id=id)
    detailed_serialized_project = DetailedProjectSerializer(project)
    return Response(detailed_serialized_project.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def api_create_project(request):
    project_serializer = ProjectSerializer(data=request.data)
    if project_serializer.is_valid():
        project_serializer.save()
        return Response(project_serializer.data, status=status.HTTP_201_CREATED)
    return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def api_update_project(request, id):
    project = Project.objects.get(id=id)
    project_serializer = ProjectSerializer(instance=project, data=request.data)
    if project_serializer.is_valid():
        project_serializer.save()
        return Response(project_serializer.data, status=status.HTTP_200_OK)
    return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return Response('Project deleted', status=status.HTTP_200_OK)