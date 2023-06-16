from exceptions import InvalidArgument
from types_lang import Id

class Memory:
    def __init__(self) -> None:
        self.box : dict[str, any] = {}

    def __getitem__(self, key : Id):
        if key.value in self.box:
            return self.box[key.value]
        raise InvalidArgument("variable is not defined")
    
    def __setitem__(self, key : Id , value):
        if key.value in self.box and type(value) is not type(self.box[key.value]):
            raise InvalidArgument("assigning a declared variable an argument of a different type")
        self.box[key.value] = value

    def contains(self, key : Id) -> bool:
        return key.value in self.box
    