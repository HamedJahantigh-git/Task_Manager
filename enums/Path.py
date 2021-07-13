from enum import Enum


class Path(Enum):
    RESOURCE = "resource"
    USER = RESOURCE + "/USER"
