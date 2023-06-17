class ScriptNotFound(Exception):
    def __init__(self, message):
        self.message = message


class WrongNumberArguments(Exception):
    def __init__(self, message):
        self.message = message


class InvalidArgument(Exception):
    def __init__(self, message):
        self.message = message
