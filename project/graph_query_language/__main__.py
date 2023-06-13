import sys
from exceptions import ScriptNotFound
from exceptions import WrongNumberArguments
from exceptions import InvalidArgument
from interpreter import interpreter
from pathlib import Path

def read_file(file: Path)-> str:
    text = file.open()
    return "".join(text.readlines())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise WrongNumberArguments("file name not passed")
    file = Path(sys.argv[1])
    if not file.is_file():
        raise ScriptNotFound("the given name is not exists")
    if not file.name.endswith(".lng"):
        raise InvalidArgument("invalid file format")
    interpreter(read_file(file))
