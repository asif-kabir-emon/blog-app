# Generated by Django 5.0.6 on 2024-06-08 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authors", "0001_initial"),
        ("posts", "0002_alter_post_author"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Author",
        ),
    ]