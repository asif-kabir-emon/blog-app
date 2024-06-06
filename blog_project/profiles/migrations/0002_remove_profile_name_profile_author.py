# Generated by Django 5.0.6 on 2024-06-06 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authors", "0001_initial"),
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="name",
        ),
        migrations.AddField(
            model_name="profile",
            name="author",
            field=models.OneToOneField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="authors.author",
            ),
        ),
    ]