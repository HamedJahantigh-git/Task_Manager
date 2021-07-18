from enum import Enum


class MessageEnum(Enum):
    EXIT = "Exit"
    INVALID = "Invalid Input!!! Please Try Again"
    SUCCESSFUL = " Successful Action"
    EXIT_MESSAGE = " Finish!!! Thanks for using"
    ENTER_COMMAND = " - Enter Your Command: "
    DB_CONNECTION_ERROR = "Connection Mistake"
    PROJECT_NAME_REPETITIVE = "Project Name is Repetitive"
    PROJECT_NAME_INVALID = "Project isn't Exist"
