from antlr4 import *
from antlr4.InputStream import InputStream

# from project.graph_query_language.language.LanguageLexer import LanguageLexer
# from project.graph_query_language.language.LanguageParser import LanguageParser
from language.LanguageLexer import LanguageLexer
from language.LanguageParser import LanguageParser


def build_parser(text: str) -> LanguageParser:
    data = InputStream(text)
    lexer = LanguageLexer(data)
    stream = CommonTokenStream(lexer)
    return LanguageParser(stream)


def check_input(text: str) -> bool:
    parser = build_parser(text)
    parser.program()
    return parser.getNumberOfSyntaxErrors() == 0


print(check_input('z :="ff";'))
print(check_input("z :=124124;"))
print(check_input("z124_asd :=124124;"))

print(check_input('edge :=(1, "ss", 1123);'))

print(check_input('edge :={41, "1", "asda"};'))
print(check_input('bool :={true, false, "asda"};'))

print(
    check_input(
        'g :=({(1, "ss", 1123), (1, "ss", 1123), (1, "ss", 1123)}, {1, 2, 3, 4, 5});'
    )
)

print(check_input("f :=(lambda {x, y} -> xy);"))

print(check_input("f := a ;//of 1 to 1;"))
print(check_input("f := (set_start of asd to s);//of 1 to 1;"))

print(check_input("f := (add_start of asd to s);//of 1 to 1;"))

print(check_input("f := (set_final of asd to s);//of 1 to 1;"))

print(check_input("f := (add_final of asd to s);//of 1 to 1;"))

print(check_input("f := (get_final of asd);//of 1 to 1;"))
print(check_input("f := (get_start of asd);//of 1 to 1;"))
print(check_input("f := (get_reachable of asd);//of 1 to 1;"))
print(check_input("f := (get_vertices of asd);//of 1 to 1;"))
print(check_input("f := (get_edges of asd);//of 1 to 1;"))
print(check_input("f := (get_labels of asd);//of 1 to 1;"))

print(check_input("f := (map (lambda {x, y} -> xy) asd);//of 1 to 1;"))
print(check_input("f := (filter (lambda {x, y} -> xy) asd);//of 1 to 1;"))

print(check_input('f := (load "sorce");//of 1 to 1;'))

print(check_input("f := g1 & g2;//of 1 to 1;"))
print(check_input("f := g1 . g2;//of 1 to 1;"))
print(check_input("f := g1 | g2;//of 1 to 1;"))
print(check_input("f := g1 in g2;//of 1 to 1;"))
print(check_input("f := g1*;//of 1 to 1;"))
