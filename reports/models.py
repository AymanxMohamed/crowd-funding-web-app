from django.db import models

# Create your models here.

class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    related_project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, null=True, blank=True)
    related_comment = models.ForeignKey('comments.Comment', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']