from django.contrib import admin

# Register your models here.

from categories.models import Category
from comments.models import Comment
from users.models import User
from tags.models import Tag
from donations.models import Donation
from .models import Project, Image

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Donation)
admin.site.register(Project)
admin.site.register(Image)

