# Generated by Django 5.0.6 on 2024-06-08 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0009_comment_comment_unique_post_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="posts.post",
            ),
        ),
    ]