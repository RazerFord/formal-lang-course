import sys
from project.graph_query_language.exceptions import ScriptNotFound
from project.graph_query_language.exceptions import WrongNumberArguments
from project.graph_query_language.exceptions import InvalidArgument
from project.graph_query_language.interpreter import interpreter
from project.graph_query_language.utils import print_err
from pathlib import Path


def read_file(file: Path) -> str:
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
