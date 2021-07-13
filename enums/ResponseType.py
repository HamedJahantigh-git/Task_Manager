from enum import Enum


class ResponseType(Enum):
    START = "Start"
    NEW_PROJECT = "New Project"
    NEW_TASK = "New Task"
    MY_PROJECT = "My Project"
    PROJECT_LIST = "Project List"
    PROJECT_ENTITY = "Project Entity"
    ERROR = "ERROR"
    EXIT = "Exit"
