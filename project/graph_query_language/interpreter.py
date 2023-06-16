from language_parser import build_parser
from visitor import Visitor

def interpreter(text_prog: str) -> str:
    parser = build_parser(text_prog)
    tree = parser.program()
    visitor = Visitor()

    visitor.visit(tree)
    
