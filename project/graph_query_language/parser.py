from antlr4 import *
from antlr4.InputStream import InputStream

from project.graph_query_language.language.LanguageLexer import LanguageLexer
from project.graph_query_language.language.LanguageParser import LanguageParser


def build_parser(text: str) -> LanguageParser:
    data = InputStream(text)
    lexer = LanguageLexer(data)
    stream = CommonTokenStream(lexer)
    return LanguageParser(stream)


def check_input(text: str) -> bool:
    parser = build_parser(text)
    parser.program()
    return parser.getNumberOfSyntaxErrors() == 0
