from enums.MessageEnum import MessageEnum
from enums.PrintListEnum import PrintListEnum
from enums.ResponseType import ResponseType
from model.Response import Response


class MessageHandler:

    def handle(self, exception):
        switcher = {
            MessageEnum.INVALID.value: self._invalid_input,
        }
        try:
            return switcher[exception.message]()
        except Exception as e:
            print(e)

    def _invalid_input(self):
        response = Response()
        response.type = ResponseType.ERROR
        response.print_list_type.append(PrintListEnum.ERROR)
        response.print_list_content.append(MessageEnum.INVALID.value)
        return response
