from email.policy import default
from django.db import models


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
    
    class Meta:
        ordering = ['-start_date']
        

class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='projects/static/images/', default='projects/static/images/default.jpg')


    def __str__(self):
        return self.image.url