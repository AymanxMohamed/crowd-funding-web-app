# Generated by Django 4.0.4 on 2022-05-05 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(blank=True, default='projects/static/images/default.jpg', null=True, upload_to='projects/static/images/'),
        ),
    ]