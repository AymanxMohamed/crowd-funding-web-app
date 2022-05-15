from rest_framework import serializers

from reports.models import ProjectReport, CommentReport


class ReportSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField('get_owner_name')

    def get_owner_name(self, report):
        return report.owner.first_name + " " + report.owner.last_name


class CommentReportSerializer(ReportSerializer):

    class Meta:
        model = CommentReport
        fields = "__all__"


class ProjectReportSerializer(ReportSerializer):
    related_project_title = serializers.SerializerMethodField('get_related_project_title')

    def get_related_project_title(self, report):
        return report.related_project.title

    class Meta:
        model = ProjectReport
        fields = "__all__"
