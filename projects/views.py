from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from projects.models import Project, Image
#########
from comments.models import Comment
from tags.models import Tag
from users.models import User
from categories.models import Category
#########
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