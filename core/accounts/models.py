from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser,PermissionsMixin
)


class User(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    # is_verified=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['email']

    def __str__(self):
        return self.email