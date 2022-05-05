# Generated by Django 4.0.4 on 2022-05-04 22:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_alter_image_image'),
        ('ratings', '0005_remove_rating_rating_rating_rating'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'project')},
        ),
    ]