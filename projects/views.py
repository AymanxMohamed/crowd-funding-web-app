from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum

from projects.helpers import validate_image_extension
from projects.models import Project , Image
from projects.serializers import ProjectSerializer, DetailedProjectSerializer


@api_view(['GET'])
def api_projects_list(request):
    projects = Project.objects.all()
    projects_serialized = ProjectSerializer(projects, many=True)
    if request.query_params.get('featured') == 'true':
        projects = projects.filter(is_featured=True)[:5]
        projects_serialized = ProjectSerializer(projects, many=True)
    return Response(projects_serialized.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_get_project_by_id(request, id):
    project = Project.objects.get(id=id)
    detailed_serialized_project = DetailedProjectSerializer(project)
    return Response(detailed_serialized_project.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_search_projects(request, query):
    projects = Project.objects.filter(title__icontains=query)
    serialized_projects = ProjectSerializer(projects, many=True)
    return Response(serialized_projects.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def api_create_project(request):
    project_serializer = ProjectSerializer(data=request.data)
    if project_serializer.is_valid():
        project_serializer.save()
        for image in request.FILES.getlist('images'):
            validate_image_extension(image)
            Image.objects.create(project_id=project_serializer.data['id'], image=image)
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
    if project.donation_set.aggregate(Sum('amount'))['amount__sum'] > project.total_target * 0.25:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    project.delete()
    return Response('Project deleted', status=status.HTTP_200_OK)




@api_view(['POST'])
def project_images(request, id):
    for image in request.FILES.getlist('images'):
        validate_image_extension(image)
        Image.objects.create(project_id=id, image=image)
    return Response('Added images to project', status=status.HTTP_200_OK)