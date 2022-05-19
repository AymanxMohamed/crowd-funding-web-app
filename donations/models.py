from django.db import models
from server import settings
from django.core.validators import MinValueValidator
from users.models import User
# Create your models here.


class Donation(models.Model):
    project = models.ForeignKey(to='projects.Project', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    message = models.TextField(blank=True,max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + '-' + self.amount.__str__()
