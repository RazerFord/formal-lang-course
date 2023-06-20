from antlr4 import *
from antlr4.InputStream import InputStream
from antlr4.error.Errors import ParseCancellationException
from antlr4.tree.Tree import TerminalNodeImpl

from pydot import Dot, Edge, Node

from project.graph_query_language.language.LanguageLexer import LanguageLexer
from project.graph_query_language.language.LanguageParser import LanguageParser
from project.graph_query_language.language.LanguageListener import LanguageListener


def build_parser(text: str) -> LanguageParser:
    """
    Parameters
    ----------
        text: str
            Text to check
    Returns
    ----------
        bool
            Built parser
    """
    data = InputStream(text)
    lexer = LanguageLexer(data)
    stream = CommonTokenStream(lexer)
    return LanguageParser(stream)


def check_input(text: str) -> bool:
    """
    Parameters
    ----------
        text: str
            Text to check
    Returns
    ----------
        bool
            true if it matches grammar vs false
    """
    parser = build_parser(text)
    parser.program()
    return parser.getNumberOfSyntaxErrors() == 0


class TreeListener(LanguageListener):
    def __init__(self, text: str):
        """
        Parameters
        ----------
            text: str
                Text to check
            Returns
        ----------
        """
        parser = build_parser(text)
        self.ast = parser.program()
        if parser.getNumberOfSyntaxErrors() != 0:
            raise ParseCancellationException("fail parse")
        self.tree = Dot("tree", graph_type="digraph")
        self.number_nodes = 0
        self.nodes = {}
        self.rules = LanguageParser.ruleNames
        super(TreeListener, self).__init__()

    def save_in_dot(self, path: str):
        """
        Parameters
        ----------
            path: str
                path for save of graph
        Returns
        ----------
        """
        ParseTreeWalker().walk(self, self.ast)
        self.tree.write(str(path))

    def enterEveryRule(self, rule: ParserRuleContext):
        """
        Parameters
        ----------
            rule: ParserRuleContext
                rule for parser
        Returns
        ----------
        """
        if rule not in self.nodes:
            self.number_nodes += 1
            self.nodes[rule] = self.number_nodes
        if rule.parentCtx:
            self.tree.add_edge(Edge(self.nodes[rule.parentCtx], self.nodes[rule]))
        label = self.rules[rule.getRuleIndex()]
        self.tree.add_node(Node(self.nodes[rule], label=label))

    def visitTerminal(self, term: TerminalNodeImpl):
        """
        Parameters
        ----------
            term: TerminalNodeImpl
                TerminalNodeImpl for visit
        Returns
        ----------
        """
        self.number_nodes += 1
        self.tree.add_edge(Edge(self.nodes[term.parentCtx], self.number_nodes))
        self.tree.add_node(Node(self.number_nodes, label=f"Terminal: {term.getText()}"))
