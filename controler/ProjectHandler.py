from Exeption.Error import InvalidInput
from controler.FileManager import FileManager
from enums.CommandEnum import CommandEnum
from enums.PrintListEnum import PrintListEnum
from enums.ResponseType import ResponseType
from model.Response import Response
from model.Task import Task


class ProjectHandler:

    def __init__(self):
        self._processor = None
        self._fileManager = FileManager()

    def set_processor(self, processor):
        self.processor = processor

    def handle(self, value):
        switcher = {
            CommandEnum.PROJECT_LIST.value: self._state_to_project_list,
            CommandEnum.NEW_TASK.value: self._state_to_new_task,
            CommandEnum.BACK.value: self._back,
        }
        try:
            return switcher[value]()
        except:
            raise InvalidInput

    def _state_to_project_list(self):
        self.processor.state.type = CommandEnum.PROJECT_LIST
        response = Response()
        response.type = ResponseType.PROJECT_LIST
        response.print_list_type.append(PrintListEnum.HEADER)
        response.print_list_content.append(CommandEnum.PROJECT_LIST.value)
        response.print_list_type.append(PrintListEnum.MENU)
        response.print_list_content.append(self.processor.user.projects_list_name())
        response.is_input = True
        response.is_list_input = False
        return response

    def project_list(self, value):
        if value not in self.processor.user.projects_list_name():
            raise InvalidInput
        self.processor.state.type = CommandEnum.PROJECT_ENTITY
        response = Response()
        response.print_list_type.append(PrintListEnum.HEADER)
        response.print_list_content.append(CommandEnum.PROJECT_ENTITY.value + ": " + value)
        response.print_list_type.append(PrintListEnum.MENU)
        response.print_list_content.append(self.processor.user.projects_list_name())
        response.is_input = False
        response.is_list_input = False
        return response

    def project_entity(self, value):
        if value not in self.processor.user.projects_list_name():
            raise InvalidInput
        self.processor.state.type = CommandEnum.MAIN_MENU
        response = Response()
        response.type = ResponseType.PROJECT_ENTITY
        response.print_list_type.append(PrintListEnum.PROJECT_ENTITY)
        response.print_list_content = [self.processor.user.get_project(value).entity()]
        response.is_input = False
        response.is_list_input = False
        return response

    def _state_to_new_task(self):
        self.processor.state.type = CommandEnum.NEW_TASK
        response = Response()
        response.type = ResponseType.NEW_TASK
        response.type = ResponseType.NEW_PROJECT
        response.print_list_type.append(PrintListEnum.SPECIFICATIONS)
        response.print_list_content.append(CommandEnum.NEW_Task_RESPONSE.value)
        response.is_input = False
        response.is_list_input = True
        return response

    def new_task(self, value):
        if value[3] not in self.processor.user.projects_list_name():
            raise InvalidInput
        task = Task(value[0], value[1], value[2])
        self.processor.user.get_project(value[3]).tasks_list.append(task)
        return self.processor.main_menu_handler.state_to_my_project()

    def _back(self):
        return self.processor.start(None)
