from pyformlang.cfg import Production, Variable, Terminal, CFG, Epsilon
from typing import AbstractSet, Iterable
from pyformlang.cfg.utils import to_variable, to_terminal
from pyformlang.regular_expression import Regex
from pyformlang import rsa
from context_free_grammar import read_cfg_from_file

# from pyformlang.cfg import Production, Variable, Terminal, CFG, Epsilon


class ECFG:
    def __init__(
        self,
        variables: AbstractSet[Variable] = None,
        terminals: AbstractSet[Terminal] = None,
        start_symbol: Variable = None,
        productions: Iterable[Production] = None,
    ):
        if variables is not None:
            variables = {to_variable(x) for x in variables}
        self._variables = set(variables) or set()
        if terminals is not None:
            terminals = {to_terminal(x) for x in terminals}
        self._terminals = set(terminals) or set()
        if start_symbol is not None:
            start_symbol = to_variable(start_symbol)
            self._variables.add(start_symbol)
        self._start_symbol = start_symbol
        self._productions = productions

    @property
    def productions(self):
        return self._productions

    @property
    def start_symbol(self):
        return self._start_symbol

    @property
    def terminals(self):
        return self._terminals

    @property
    def variables(self):
        return self._variables

    def to_rsm(self):
        print(list(self._productions))
        boxes = [rsa.Box(e.head, e.body) for e in list(self._productions)]
        return rsa(self._variables.self._start_symbol, boxes)

    @staticmethod
    def from_cfg(cfg: CFG):
        variables = cfg.variables
        terminals = cfg.terminals
        start_symbol = cfg.start_symbol
        productions = {}
        for prod in cfg.productions:
            if prod.head in productions:
                raise OneRuleError()
            body = prod.body
            if len(body) != 0:
                body = "".join(str(x.value) for x in prod.body)
            else:
                body = "$"
            productions[prod.head] = body
        prods = set()
        for n, p in productions.items():
            prods.add(Production(n, [Regex(p)]))
        return ECFG(variables, terminals, start_symbol, prods)

    @staticmethod
    def from_file(name_file: str):
        return ECFG.from_cfg(read_cfg_from_file(name_file))

    @staticmethod
    def from_str(text: str):
        return ECFG.from_cfg(CFG.from_text(text))


class OneRuleError(Exception):
    def __init__(self) -> None:
        super().__init__("Only one rule can exist for a non-terminal")


S = Variable("S")
A = Variable("A")
B = Variable("B")
a = Terminal("a")
b = Terminal("b")
prods = []
prods.append(Production(S, [A, S, A]))
# prods.append(Production(S, [a, B]))
prods.append(Production(A, [B]))
# prods.append(Production(A, [S]))
# prods.append(Production(B, [b]))
prods.append(Production(B, [Epsilon()]))
cfg = CFG(
    {S, A, B},
    {a, b},
    S,
    set(prods),
)
f = ECFG.from_cfg(cfg)
f.to_rsm()
