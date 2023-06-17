from project.graph_query_language.exceptions import InvalidArgument
from project.graph_query_language.types_lang import Id

class Memory:
    def __init__(self) -> None:
        self.box : dict[str, any] = {}

    def __getitem__(self, key : Id):
        return self.get(key.value)
    
    def __setitem__(self, key : Id , value):
        if key.value in self.box and type(value) is not type(self.box[key.value]):
            raise InvalidArgument(f"assigning a declared variable an argument of a different type: {type(value)}, {type(self.box[key.value])}")
        self.box[key.value] = value

    def contains(self, key : Id) -> bool:
        return key.value in self.box
    
    def get(self, key: str) -> bool:
        if key in self.box:
            return self.box[key]
        raise InvalidArgument(f"variable '{key}' is not defined")
