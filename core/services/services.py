import os
from uuid import uuid1

from core.dataclasses import ProfileDataClass, CarDataClass


def upload_avatar(profile: ProfileDataClass, file: str) -> str:
    ext = file.split('.')[-1]
    return os.path.join(profile.surname, 'avatars', f'{uuid1()}.{ext}')


def upload_car_image(car: CarDataClass, file: str) -> str:
    ext = file.split('.')[-1]
    return os.path.join('cars', f'{car.model}_{car.year}.{ext}')
