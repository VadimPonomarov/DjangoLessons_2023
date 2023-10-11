from django.db import models

from core.models import BaseModel
from ..users.models import UserModel


class AutoParksModel(BaseModel):
    name = models.CharField(max_length=25)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')

    class Meta:
        db_table = 'autoparks'
