from enums.PrintListEnum import PrintListEnum
from enums.ResponseType import ResponseType
from model.Response import Response


class MessageHandler:

    def handle(self, exception):
        response = Response()
        response.type = ResponseType.ERROR
        response.print_list_type.append(PrintListEnum.ERROR)
        if exception.message is not None:
            response.print_list_content.append(exception.message)
        else:
            print(exception)
        return response
