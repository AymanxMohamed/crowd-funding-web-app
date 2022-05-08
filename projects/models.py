from django.db import models
from users.models import User


class Project(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    total_target = models.PositiveIntegerField()
    tags = models.ManyToManyField(to='tags.Tag', related_name='tags', blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(to='categories.Category', on_delete=models.CASCADE, default=None, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-start_date']


class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255, blank=True)
    image = models.FileField(upload_to='projects/static/images/', default='projects/static/images/default.jpg', blank=True, null=True)

    def __str__(self):
        return self.image.url
    @property
    def image_name(self):
        return self.image.__str__().split("/")[-1]