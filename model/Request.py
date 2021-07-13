from enums.RequestType import RequestType


class Request:

    def __init__(self):
        self.type = RequestType.START
        self.input_value = None
        self.last_type = None

    def print(self):
        print(self.type)
        print(self.input_value)
