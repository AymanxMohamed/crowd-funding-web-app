# Generated by Django 4.0.4 on 2022-05-04 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_alter_rating_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
    ]
