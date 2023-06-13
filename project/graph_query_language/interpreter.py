from language_parser import build_parser

def interpreter(text_prog: str) -> str:
    parser = build_parser(text_prog)
    tree = parser.program()