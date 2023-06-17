from language_parser import build_parser
from visitor import Visitor
from utils import print_err

def interpreter(text_prog: str) -> str:
    parser = build_parser(text_prog)
    tree = parser.program()
    visitor = Visitor()

    if parser.getNumberOfSyntaxErrors() != 0:
        print_err("syntax errors found")
    try:
        visitor.visit(tree)
    except Exception as e:
        print_err(e.__str__())
    
