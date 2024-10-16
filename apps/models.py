from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CharField


class User(AbstractUser):
    email = CharField(max_length=255)