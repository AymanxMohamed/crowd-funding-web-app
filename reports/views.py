from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from reports.models import Report
from reports.serializers import ReportSerializer

@api_view(['GET'])
def api_reports_list(request):
    reports = Report.objects.all()
    serializer_reports = ReportSerializer(reports, many=True)
    return Response(serializer_reports.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def api_get_report_by_id(request, pk):
    report = get_object_or_404(Report, id=pk)
    serialized_report = ReportSerializer(report)
    return Response(serialized_report.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def api_create_report(request):
    serialized_report = ReportSerializer(data=request.data)
    if serialized_report.is_valid():
        serialized_report.save()
        return Response(serialized_report.data, status=status.HTTP_201_CREATED)
    return Response(serialized_report.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['delete'])
def api_delete_report(request, pk):
    report = get_object_or_404(Report, id=pk)
    report.delete()
    return Response('Report deleted', status=status.HTTP_200_OK)