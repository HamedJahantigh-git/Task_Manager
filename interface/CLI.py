import math

from Exeption.Error import InvalidInput
from controler.CommandHandler import CommandHandler
from enums.CommandEnum import CommandEnum
from enums.Constant import Constant
from enums.MessageEnum import MessageEnum
from enums.PrintListEnum import PrintListEnum
from enums.RequestType import RequestType
from enums.ResponseType import ResponseType
from model.Request import Request
from model.Response import Response


class CLI:

    def __init__(self):
        self._command_handler = CommandHandler("admin")
        self._CLIWide = Constant.MENU_SIZE.value
        self._request = Request()
        self._response = Response()
        self._prev_response = self._response

    def start(self):
        while self._response.type is not ResponseType.EXIT:
            if self._response.type is not ResponseType.ERROR:
                self._prev_response = self._response
                self._response = self._command_handler.receive(self._request)
            else:
                self._response = self._prev_response

            self._response_handler(self._response)

    def _response_handler(self, response):
        count = 0
        for i in response.print_list_type:
            self._print_list_detector(i, response.print_list_content[count])
            count += 1
        if response.is_input:
            request = Request()
            request.type = RequestType.INPUT
            request.input_value = input(MessageEnum.ENTER_COMMAND.value)
            self._request = request

    def _print_list_detector(self, type, arg):
        switcher = {
            PrintListEnum.HEADER: self._printHeader,
            PrintListEnum.MENU: self._printMenu,
            PrintListEnum.SPECIFICATIONS: self._handle_spec,
            PrintListEnum.PROJECT_ENTITY: self._project_entity_print,
            PrintListEnum.ERROR: self._error_panle,
        }
        switcher[type](arg)

    def _printHeader(self, title):
        self._line_for(Constant.MENU_CHAR.value, self._CLIWide)
        print("\n" + Constant.MENU_CHAR.value, end='')
        self._line_for(" ", math.floor((self._CLIWide - 2 - len(title)) / 2))
        print(title, end='')
        self._line_for(" ", math.ceil((self._CLIWide - len(title)) / 2))
        print(Constant.MENU_CHAR.value)
        self._line_for(Constant.MENU_CHAR.value, self._CLIWide)
        print()
        return None

    def _printMenu(self, commandList):
        self._line_for(Constant.MENU_COMMANDS_CHAR.value, self._CLIWide)
        for i in commandList:
            print("\n" + "|" + Constant.MENU_COMMANDS_CHAR.value, i, end='')
            self._line_for(" ", (self._CLIWide - 4 - len(i)))
            print("|", end='')
        print("")
        self._line_for(Constant.MENU_COMMANDS_CHAR.value, self._CLIWide)
        print()
        return None

    def _handle_spec(self, list_content):
        ans_list = []
        request = Request()
        for i in list_content:
            ans_list.append(input(" - " + i + ": "))
        request.type = RequestType.INPUT_LIST
        request.input_value = ans_list
        self._request = request

    def _project_entity_print(self, value):
        print("Response ::")
        print("\t Project Name:" + value[0])
        print("\t Project Description:" + value[1])
        for i in value[2]:
            print("\t\t Task Name: " + i.name)
            print("\t\t\t Task Description: "+i.description)
            print("\t\t\t Task Date: " + i.date)
        request = Request()
        request.type = RequestType.INPUT
        request.input_value = CommandEnum.MY_PROJECT.value
        self._request = request

    def _error_panle(self, message):
        print(" *** " + message + " ***")

    def _line_for(self, str, repeat):
        for i in range(1, repeat):
            print(str, end='')
