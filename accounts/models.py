from django.contrib.auth.models import AbstractUser
from django.db import models
from base.models import BaseModel


class User(BaseModel, AbstractUser):
    email = models.EmailField(unique=True)
    is_processed = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
