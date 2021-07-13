from enums.ResponseType import ResponseType


class Response:

    def __init__(self):
        self.type = ResponseType.START
        self.print_list_type = []
        self.print_list_content = []
        self.is_input = False
        self.is_list_input = False
        self.error = None

    def print(self):
        print(self.type)
        print(self.print_list_type)
        print(self.print_list_content)
