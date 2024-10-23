from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    image = models.FileField(upload_to='images_users',blank=True,null=True)

    def __str__(self):
        return self.username
