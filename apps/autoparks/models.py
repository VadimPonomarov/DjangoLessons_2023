from django.db import models

from core.models import BaseModel


class AutoParksModel(BaseModel):
    name = models.CharField(max_length=25)

    class Meta:
        db_table = 'autoparks'
