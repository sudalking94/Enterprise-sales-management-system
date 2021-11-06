from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import UserManager, BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, name, password, **extra_fields):
        if not name:
            raise ValueError('The given name must be set')
        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(name, password, **extra_fields)
