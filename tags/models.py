from django.db import models

from projects.models import Project


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_projects_by_tag(self):
        return Project.objects.filter(tags__in=[self])

    def __str__(self):
        return self.name
