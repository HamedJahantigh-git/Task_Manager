from DataBase.DB import DB
from controler.FileManager import FileManager
from controler.MainMenuHandler import MainMenuHandler
from controler.NewProjectHandler import NewProjectHandler
from controler.ProjectHandler import ProjectHandler
from enums.CommandEnum import CommandEnum
from enums.MessageEnum import MessageEnum
from enums.PrintListEnum import PrintListEnum
from enums.ResponseType import ResponseType
from model.Response import Response
from model.State import State


class Processor:

    def __init__(self, username):
        self.db = DB()
        self.db.initialize()
        self.user = self.db.load_user(username)
        self.state = State()
        self.main_menu_handler = MainMenuHandler()
        self.new_project_handler = NewProjectHandler()
        self.project_handler = ProjectHandler()

    def setter(self):
        self.main_menu_handler.set_processor(self)
        self.new_project_handler.set_processor(self)
        self.project_handler.set_processor(self)

    def start(self, *arg):
        self.state.type = CommandEnum.MAIN_MENU
        response = Response()
        response.print_list_type.append(PrintListEnum.HEADER)
        response.print_list_content.append(CommandEnum.MAIN_MENU.value)
        response.print_list_type.append(PrintListEnum.MENU)
        response.print_list_content.append(CommandEnum.MAIN_MENU_CONTENT.value)
        response.is_input = True
        response.is_list_input = False
        return response

    def exit(self, *arg):
        response = Response()
        response.type = ResponseType.EXIT
        response.print_list_type.append(PrintListEnum.HEADER)
        response.print_list_content.append(MessageEnum.EXIT_MESSAGE.value)
        self.db.exit()
        return response
