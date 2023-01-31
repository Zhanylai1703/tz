from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.models import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True, default = "")
    email = models.EmailField(unique=True, db_index=True, default = "")
    first_name = models.CharField(max_length=30, blank=True, default = "")
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


    objects = UserManager()





# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.translation import gettext_lazy as _

# from .managers import CustomUserManager


# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_("email address"), unique=True)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email
