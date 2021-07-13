from enums.MessageEnum import MessageEnum
from enums.CommandEnum import CommandEnum


class InvalidInput(Exception):
    def __init__(self):
        self.expression = CommandEnum.INVALID.value
        self.message = MessageEnum.INVALID.value


class UndefinedError(Exception):
    def __init__(self):
        self.expression = CommandEnum.UNDEFINED_ERROR.value
        self.message = MessageEnum.INVALID.value
