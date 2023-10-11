from django.db import models
from django.core import validators as V

from core.models import BaseModel


class UserModel(BaseModel):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25, unique=True, validators=[V.EmailValidator()])
    class Meta:
        db_table = 'users'
