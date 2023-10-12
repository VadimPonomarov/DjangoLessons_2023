from enum import Enum


class RegEx(Enum):
    NAME = (
        r'^[A-ZА-Z][A-z\d]{2,24}$',
        'First capital min 3 max 25'
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.msg = msg
        self.pattern = pattern
