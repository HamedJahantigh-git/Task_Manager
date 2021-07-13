from enum import Enum


class CommandEnum(Enum):
    MAIN_MENU = "Main Menu"
    NEW_PROJECT = "New Project"
    MY_PROJECT = "My Projects"
    EXIT = "Exit"
    MAIN_MENU_CONTENT = [NEW_PROJECT, MY_PROJECT, EXIT]

    PROJECT_LIST = "Projects List"
    NEW_TASK = "New Task"
    BACK = "Back"
    MY_PROJECT_COMMANDS = [PROJECT_LIST, NEW_TASK, BACK]

    PROJECT_NAME = "Project Name"
    PROJECT_DESCRIPTION = "Project Description"
    New_PROJECT_CONTENT = ["Please Complete the Following Requirements"]
    NEW_PROJECT_RESPONSE = [PROJECT_NAME, PROJECT_DESCRIPTION]

    TASK_NAME = "Task Name"
    TASK_DESCRIPTION = "Task Description"
    TASK_DATE = "Date"
    NEW_Task_RESPONSE = [TASK_NAME, TASK_DESCRIPTION, TASK_DATE, PROJECT_NAME]

    INVALID = "Invalid"
    UNDEFINED_ERROR = "Undefined Error"
    SUCCESSFUL = "Successful"

    PROJECT_ENTITY = "Project Entity"
