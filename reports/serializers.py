from rest_framework import serializers

from reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField('get_owner')
    related_project = serializers.SerializerMethodField('get_related_project')
    
    def get_owner(self, report):
        return report.owner.first_name + " " + report.owner.last_name
    
    def get_related_project(self, report):
        return report.related_project.title
    
    
    class Meta:
        model = Report
        fields = "__all__"
        
        