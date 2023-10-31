from enum import Enum


class UserRegEx(Enum):
    NAME_SURNAME = (
        r'^[A-zА-Я]\w{2,24}$',
        'Name is a string. First letter is capitalized, min 3 max 25 characters'
    )
    PASSWORD = (
        r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{6,}$',
        'Checks that a password has a minimum of 6 characters, at least 1 uppercase letter, 1 lowercase letter, and 1 number with no spaces.'
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.msg = msg
        self.pattern = pattern
