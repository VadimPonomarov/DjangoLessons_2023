from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V

from core.models import BaseModel
from .managers import UserManager
from .regex import UserRegEx
from django.db import models


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'
        ordering = ['id']

    name = models.CharField(max_length=25,
                            validators=[V.RegexValidator(UserRegEx.NAME_SURNAME.pattern, UserRegEx.NAME_SURNAME.msg)])
    surname = models.CharField(max_length=25, validators=[
        V.RegexValidator(UserRegEx.NAME_SURNAME.pattern, UserRegEx.NAME_SURNAME.msg)])
    age = models.IntegerField()


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'
        ordering = ['id']

    email = models.EmailField(unique=True, validators=[V.EmailValidator])
    password = models.CharField(max_length=255,
                                validators=[V.RegexValidator(UserRegEx.PASSWORD.pattern, UserRegEx.PASSWORD.msg)])
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='user', null=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()
