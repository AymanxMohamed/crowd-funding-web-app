from django.db import models

# Create your models here.


class Report(models.Model):
    details = models.TextField()
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class CommentReport(Report):
    related_comment = models.ForeignKey('comments.Comment', on_delete=models.CASCADE, blank=True)


class ProjectReport(Report):
    related_project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
