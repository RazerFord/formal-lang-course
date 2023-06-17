import sys


def print_err(msg: str):
    print("\033[31m" + msg.__str__())
    sys.exit(1)
