from django.db import models
from django.core import validators as V

from core.models import BaseModel
from .regEx import RegEx
from ..users.models import UserModel


class AutoParksModel(BaseModel):
    name = models.CharField(max_length=25)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks', null=True)

    class Meta:
        db_table = 'autoparks'
        ordering = ['id']
