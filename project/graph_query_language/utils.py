import sys


def print_err(msg: str, test: bool = False):
    print("\033[31m" + msg.__str__())
    if not test:
        sys.exit(1)
