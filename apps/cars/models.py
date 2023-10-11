import datetime

from django.db import models

from apps.autoparks.models import AutoParksModel
from django.core import validators as V

from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=25, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(25)])
    year = models.IntegerField(validators=[V.MaxValueValidator(datetime.datetime.now().year)])
    price = models.FloatField()
    auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')
