# Generated by Django 5.1.2 on 2024-10-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0005_posts_costs"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="posts",
            name="costs",
        ),
        migrations.AddField(
            model_name="services",
            name="costs",
            field=models.PositiveIntegerField(default=5000),
            preserve_default=False,
        ),
    ]
