# Generated by Django 5.1.2 on 2024-10-22 02:18

import product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Posts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pet_name", models.CharField(max_length=120)),
                ("date", models.DateField()),
                (
                    "phone",
                    models.CharField(
                        max_length=12, validators=[product.models.validate_number]
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Services",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40, unique=True)),
                ("slug", models.SlugField(max_length=30, unique=True)),
                ("description", models.TextField()),
                ("image", models.FileField(upload_to="uslugi_photo")),
                ("is_push", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Time",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time",
                    models.CharField(
                        max_length=10,
                        unique=True,
                        validators=[product.models.validator_time],
                    ),
                ),
            ],
        ),
    ]
