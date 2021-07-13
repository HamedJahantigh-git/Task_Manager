from Exeption.Error import InvalidInput
from enums.CommandEnum import CommandEnum
from enums.PrintListEnum import PrintListEnum
from enums.ResponseType import ResponseType
from model.Response import Response


class MainMenuHandler:

    def __init__(self):
        self.processor = None

    def set_processor(self, processor):
        self.processor = processor

    def handle(self, value):
        switcher = {
            CommandEnum.NEW_PROJECT.value: self._state_to_new_project,
            CommandEnum.MY_PROJECT.value: self.state_to_my_project,
            CommandEnum.EXIT.value: self.processor.exit,
        }

        try:
            return switcher[value]()
        except:
            raise InvalidInput


    def state_to_my_project(self):
        self.processor.state.type = CommandEnum.MY_PROJECT
        response = Response()
        response.type = ResponseType.MY_PROJECT
        response.print_list_type.append(PrintListEnum.HEADER)
        response.print_list_content.append(CommandEnum.MY_PROJECT.value)
        response.print_list_type.append(PrintListEnum.MENU)
        response.print_list_content.append(CommandEnum.MY_PROJECT_COMMANDS.value)
        response.is_input = True
        response.is_list_input = False
        return response


    def _state_to_new_project(self):
        self.processor.state.type = CommandEnum.NEW_PROJECT
        response = Response()
        response.type = ResponseType.NEW_PROJECT
        response.print_list_type.append(PrintListEnum.SPECIFICATIONS)
        response.print_list_content.append(CommandEnum.NEW_PROJECT_RESPONSE.value)
        response.is_input = False
        response.is_list_input = True
        return response


