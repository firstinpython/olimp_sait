# Generated by Django 5.1.2 on 2024-10-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_review_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="posts",
            name="costs",
            field=models.PositiveIntegerField(default=5000),
            preserve_default=False,
        ),
    ]
