# Generated by Django 4.0.4 on 2022-04-25 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='images',
        ),
    ]
