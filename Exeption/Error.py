from enums.MessageEnum import MessageEnum
from enums.CommandEnum import CommandEnum


class InvalidInput(Exception):
    def __init__(self):
        self.expression = CommandEnum.INVALID.value
        self.message = MessageEnum.INVALID.value


class ProjectNameRepititive(Exception):
    def __init__(self):
        self.expression = CommandEnum.ERROR.value
        self.message = MessageEnum.PROJECT_NAME_REPETITIVE.value


class ProjectNameInvalid(Exception):
    def __init__(self):
        self.expression = CommandEnum.ERROR.value
        self.message = MessageEnum.PROJECT_NAME_INVALID.value


class UndefinedError(Exception):
    def __init__(self):
        self.expression = CommandEnum.UNDEFINED_ERROR.value
        self.message = MessageEnum.INVALID.value
