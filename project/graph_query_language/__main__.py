import sys
from exceptions import ScriptNotFound
from exceptions import WrongNumberArguments
from exceptions import InvalidArgument
from interpreter import interpreter
from pathlib import Path
from utils import print_err


def read_file(file: Path)-> str:
    text = file.open()
    return "".join(text.readlines())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_err("file name not passed")
    if len(sys.argv) == 2:
        file = Path(sys.argv[1])
        if not file.is_file():
            print_err("the given name is not exists")
        if not file.name.endswith(".lng"):
            print_err("invalid file format")
        interpreter(read_file(file))
    if len(sys.argv) > 2:
        prog = " ".join(sys.argv[1:]) + ";"
        interpreter(prog)
