from django.db import models
from server import settings
from users.models import User

# Create your models here.


class Donation(models.Model):
    project = models.ForeignKey(to='projects.Project', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + '-' + self.amount.__str__()
