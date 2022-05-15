# Generated by Django 4.0.4 on 2022-05-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook_link',
            field=models.TextField(default=None, null=True),
        ),
    ]
