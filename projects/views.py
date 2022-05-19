from rest_framework import status, authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError



from projects.helpers import validate_image_extension
from projects.models import Project, Image
from projects.serializers import ProjectSerializer, DetailedProjectSerializer


@api_view(['GET'])
def api_all_projects(request):
    projects = Project.objects.all()
    projects_serialized = ProjectSerializer(projects, many=True)
    return Response(projects_serialized.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_featured_projects(request):
    projects = Project.objects.filter(is_featured=True)[:5]
    projects_serialized = ProjectSerializer(projects, many=True)
    return Response(projects_serialized.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_latest_projects(request):
    projects = Project.objects.order_by('-start_date')[:5]
    projects_serialized = ProjectSerializer(projects, many=True)
    return Response(projects_serialized.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def api_projects_by_category(request,id):
    projects = Project.objects.filter(category_id=id)
    projects_serialized = ProjectSerializer(projects, many=True)
    return Response(projects_serialized.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_my_projects(request):
    projects = Project.objects.filter(owner=request.user)
    projects_serialized = ProjectSerializer(projects, many=True)
    return Response(projects_serialized.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_get_project_by_id(request, id):
    project = get_object_or_404(Project, id=id)
    detailed_serialized_project = DetailedProjectSerializer(project)
    return Response(detailed_serialized_project.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_search_projects(request, query):
    projects = Project.objects.filter(title__icontains=query)
    serialized_projects = ProjectSerializer(projects, many=True)
    return Response(serialized_projects.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_create_project(request):
    updated_request = request.POST.copy()
    updated_request.update({'owner': request.user.id})

    project_serializer = ProjectSerializer(data=updated_request)
    if project_serializer.is_valid():
        project_serializer.save()
        for image in request.FILES.getlist('images'):
            if (validate_image_extension(image)) is False:
                raise ValidationError('Invalid image extension')
            Image.objects.create(project_id=project_serializer.data['id'], image=image)
        return Response(project_serializer.data, status=status.HTTP_201_CREATED)
    return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_update_project(request, id):
    project = Project.objects.get(id=id)
    if project.owner_id != request.user.id:
        return Response({"message": "Not Authorized"}, status=status.HTTP_401_UNAUTHORIZED)
    updated_request = request.POST.copy()
    updated_request.update({'owner': request.user.id})

    project_serializer = ProjectSerializer(instance=project, data=updated_request)
    if project_serializer.is_valid():
        project_serializer.save()
        return Response(project_serializer.data, status=status.HTTP_200_OK)
    return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_project(request, id):
    project = Project.objects.get(id=id)
    if project.owner_id != request.user.id:
        return Response({"message": "Not Authorized"}, status=status.HTTP_401_UNAUTHORIZED)
    total_donations = project.donation_set.aggregate(Sum('amount'))['amount__sum']
    if total_donations and (total_donations > project.total_target * 0.25):
        return Response({"message": "Failed to delete, Donations Exceeded 25% of target."},status=status.HTTP_400_BAD_REQUEST)
    project.delete()
    return Response('Project deleted', status=status.HTTP_200_OK)


###############################################################################
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def project_images(request, id):
    for image in request.FILES.getlist('images'):
        if (validate_image_extension(image)) is False:
            raise ValidationError('Invalid image extension')
        Image.objects.create(project_id=id, image=image)
    return Response('Added images to project', status=status.HTTP_200_OK)
