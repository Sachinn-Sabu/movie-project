# Generated by Django 4.1 on 2023-07-13 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movieapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movies",
            name="img",
        ),
    ]
