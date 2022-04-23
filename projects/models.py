from django.db import models


# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    total_target = models.IntegerField(default=0)
    tags = models.ManyToManyField(to='tags.Tag', related_name='tags')
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(to='categories.Category', on_delete=models.CASCADE)
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption