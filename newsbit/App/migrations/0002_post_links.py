# Generated by Django 4.1.5 on 2023-03-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='links',
            field=models.URLField(null=True),
        ),
    ]
