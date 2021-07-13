from Exeption.Error import InvalidInput
from controler.MessageHandler import MessageHandler
from controler.Processor import Processor
from enums.CommandEnum import CommandEnum
from enums.RequestType import RequestType
from model.Request import Request
from model.Response import Response


class CommandHandler:

    def __init__(self, username):
        self._processor = Processor(username)
        self._processor.setter()
        self._request = Request()
        self._response = Response()
        self._message_handler = MessageHandler()

    def receive(self, request):
        self._request = request
        self._response = self._request_detector()
        self._processor.file_manager.saveUser(self._processor.user)

        return self._response

    def _request_detector(self):
        switcher = {
            RequestType.START: self._processor.start,
            RequestType.INPUT: self._input_state_detector,
            RequestType.INPUT_LIST: self._input_list_state_detector
        }

        # return switcher[self._request.type](self._processor.state.type, self._request.input_value)
        try:
            return switcher[self._request.type](self._processor.state.type, self._request.input_value)
        except Exception as exception:
            return self._message_handler.handle(exception)

    def _input_state_detector(self, type, value):
        switcher = {
            CommandEnum.MAIN_MENU: self._processor.main_menu_handler.handle,
            CommandEnum.MY_PROJECT: self._processor.project_handler.handle,
            CommandEnum.PROJECT_LIST: self._processor.project_handler.project_list,
            CommandEnum.PROJECT_ENTITY: self._processor.project_handler.project_entity,
        }
        return switcher[type](value)

    def _input_list_state_detector(self, type, value):
        switcher = {
            CommandEnum.NEW_PROJECT: self._processor.new_project_handler.new_project,
            CommandEnum.NEW_TASK: self._processor.project_handler.new_task,
        }
        return switcher[type](value)

    def __checkNewProjectCommands(self):
        self._processor.newProject()

    def __checkMyProjectCommands(self):
        switcher = {
            CommandEnum.PROJECT_LIST.value: self._processor.projectList,
        }
        try:
            switcher[self.__command]()
        except:
            raise InvalidInput
