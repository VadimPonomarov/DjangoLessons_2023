import datetime

from django.db import models

from apps.autoparks.models import AutoParksModel
from django.core import validators as V

from core.models import BaseModel
from core.services import upload_car_image


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ['id']

    model = models.CharField(max_length=25, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(25)])
    year = models.IntegerField(validators=[V.MaxValueValidator(datetime.datetime.now().year)])
    price = models.FloatField()
    image = models.ImageField(upload_to=upload_car_image, blank=True)
    auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')
