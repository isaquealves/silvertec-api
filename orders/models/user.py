import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullName = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=100)