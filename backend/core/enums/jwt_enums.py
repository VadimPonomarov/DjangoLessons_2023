from enum import Enum
from datetime import timedelta
from typing import Type


class ActionTokenEnum(Enum):
    ACTIVATE = (
        'activate',
        timedelta(minutes=30)
    )
    RECOVERY = (
        'recovery',
        timedelta(minutes=30)
    )

    def __init__(self, token_type: str, lifetime: Type[timedelta]):
        self.lifetime = lifetime
        self.token_type = token_type
