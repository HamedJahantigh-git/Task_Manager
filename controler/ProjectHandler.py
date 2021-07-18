from Exeption.Error import InvalidInput, ProjectNameInvalid
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
        project_list = self.processor.db.project_list_name()
        print("project state to list")
        print(project_list)
        response.print_list_content.append(project_list)
        response.is_input = True
        response.is_list_input = False
        return response

    def project_list(self, value):
        project_list = self.processor.db.project_list_name()
        if value not in project_list:
            raise InvalidInput
        self.processor.state.type = CommandEnum.PROJECT_ENTITY
        response = Response()
        response.print_list_type.append(PrintListEnum.HEADER)
        response.print_list_content.append(CommandEnum.PROJECT_ENTITY.value + ": " + value)
        response.print_list_type.append(PrintListEnum.MENU)
        project_list = self.processor.db.project_list_name()
        response.print_list_content.append(project_list)
        response.is_input = False
        response.is_list_input = False
        return response

    def project_entity(self, value):
        project_entity = self.processor.db.project_entity(value)
        if len(project_entity) == 0:
            raise InvalidInput
        project_tasks_entity = self.processor.db.project_tasks_entity(value)
        entity = [project_entity[0][1], project_entity[0][2]]
        ans = []
        for i in project_tasks_entity:
            ans.append([i[2], i[3], i[4]])
        entity.append(ans)
        self.processor.state.type = CommandEnum.MAIN_MENU
        response = Response()
        response.type = ResponseType.PROJECT_ENTITY
        response.print_list_type.append(PrintListEnum.PROJECT_ENTITY)
        response.print_list_content = [entity]
        print(entity)
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
        task = Task(value[0], value[1], value[2])
        try:
            self.processor.db.save_new_task(value[3], task)
        except:
            # todo
            raise ProjectNameInvalid
        return self.processor.main_menu_handler.state_to_my_project()

    def _back(self):
        return self.processor.start(None)
