from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Rating(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)

    class Meta:
        unique_together = ('user', 'project')
    
    def __str__(self):
        return str(self.rating)