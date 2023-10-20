from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProfileDataClass:
    id: int
    name: str
    surname: str
    age: int
    avatar: str


@dataclass
class UserDataClass:
    id: int
    email: str
    password: str
    is_active: bool
    is_staff: bool
    is_superuser: bool
    crated_at: datetime
    updated_at: datetime
    profile: ProfileDataClass


@dataclass
class AutoparkDataClass:
    id: int
    name: str


@dataclass
class CarDataClass:
    id: int
    model: str
    year: int
    price: float
    image: str
    auto_park: AutoparkDataClass
