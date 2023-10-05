import datetime

from django.db import models

from core.models import BaseModel
from django.core import validators as V


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=25, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(25)])
    year = models.IntegerField(validators=[V.MaxValueValidator(datetime.datetime.now().year)])
    seats = models.IntegerField()
    type = models.CharField(max_length=25, validators=[V.MaxLengthValidator(25)], default='sedan')
    engine_v = models.FloatField()
