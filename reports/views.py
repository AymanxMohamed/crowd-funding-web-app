from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from reports.models import CommentReport, ProjectReport
from reports.serializers import CommentReportSerializer, ProjectReportSerializer

""" Comment Reports """


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_comment_reports(request):
    reports = CommentReport.objects.filter(owner=request.user)
    serializer_reports = CommentReportSerializer(reports, many=True)
    return Response(serializer_reports.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_comment_report_by_id(request, pk):
    report = get_object_or_404(CommentReport, id=pk)
    serialized_report = CommentReportSerializer(report)
    return Response(serialized_report.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_create_comment_report(request):
    updated_request = request.data.copy()
    updated_request.update({'owner': request.user.id})
    serialized_report = CommentReportSerializer(data=updated_request)
    if serialized_report.is_valid():
        serialized_report.save()
        return Response(serialized_report.data, status=status.HTTP_201_CREATED)
    return Response(serialized_report.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_comment_report(request, pk):
    report = get_object_or_404(CommentReport, id=pk)
    report.delete()
    return Response('Report deleted', status=status.HTTP_200_OK)


""" Project Reports """


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_project_reports(request):
    reports = ProjectReport.objects.all()
    serializer_reports = ProjectReportSerializer(reports, many=True)
    return Response(serializer_reports.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_project_report_by_id(request, pk):
    report = get_object_or_404(ProjectReport, id=pk)
    serialized_report = ProjectReportSerializer(report)
    return Response(serialized_report.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_create_project_report(request):
    updated_request = request.data.copy()
    updated_request.update({'owner': request.user.id})

    serialized_report = ProjectReportSerializer(data=updated_request)
    if serialized_report.is_valid():
        serialized_report.save()
        return Response(serialized_report.data, status=status.HTTP_201_CREATED)
    return Response(serialized_report.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_project_report(request, pk):
    report = get_object_or_404(ProjectReport, id=pk)
    report.delete()
    return Response('Report deleted', status=status.HTTP_200_OK)

