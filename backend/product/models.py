from django.db import models
from django.core.exceptions import ValidationError
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


def validate_number(phone):
    if (not str(phone).startswith("+7") or len(phone) != 12) and (not str(phone).startswith("8") or len(phone) != 11):
        raise ValidationError('Неправильно набран номер')


def validator_time(time):
    mass_time = time.split(':')
    if len(mass_time) == 2:
        for i in mass_time:
            if i.isdigit():
                ...
            else:
                raise ValidationError("Неправильно записали время ЧЧ:ММ")
    else:
        raise ValidationError("Неправильно записали время ЧЧ:ММ")


# Create your models here.
class Posts(models.Model):
    # profile = models.ForeignKey(to=User,on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.ForeignKey(to="Services", on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=120)
    date = models.DateField()
    phone = models.CharField(max_length=12, validators=[
        validate_number
    ])
    email = models.EmailField()
    time = models.ForeignKey(to="Time", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name.name}| {self.time.time}"


class Services(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(unique=True, max_length=30)
    description = models.TextField()
    image = models.FileField(upload_to='uslugi_photo')
    costs = models.PositiveIntegerField()
    is_push = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Time(models.Model):
    time = models.CharField(max_length=10, validators=[validator_time], unique=True)  # нужно поставить валидатор

    def __str__(self):
        return self.time


class HeaderThings(models.Model):
    city = models.CharField(max_length=30)
    logo = models.FileField(upload_to='logo_photo')
    title_logo = models.CharField(max_length=30, verbose_name="title")
    subtitle_logo = models.CharField(max_length=30, verbose_name='subtitle')


class Review(models.Model):
    username = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField()
    score = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    service = models.ForeignKey(to="Services", on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='logo_person',null=True)

    def __str__(self):
        return f"{self.username.username} | {self.score}"
