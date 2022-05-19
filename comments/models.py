from django.db import models
from projects.models import Project
from users.models import User

# Create your models here.


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
