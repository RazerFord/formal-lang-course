from pyformlang.cfg import Production, Variable, Terminal, CFG, Epsilon
from pyformlang.cfg.utils import to_variable, to_terminal
from pyformlang.regular_expression import Regex
from pyformlang.finite_automaton.finite_automaton import to_symbol
from context_free_grammar import read_cfg_from_file
from rsm import RSM
from functools import reduce
from typing import AbstractSet, Iterable


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
        boxes = {
            to_symbol(n.value): p.to_epsilon_nfa().minimize()
            for n, p in self._productions.items()
        }
        s = to_symbol(self._start_symbol.value)
        return RSM(s, boxes)

    @staticmethod
    def from_cfg(cfg: CFG):
        variables = cfg.variables
        terminals = cfg.terminals
        start_symbol = cfg.start_symbol
        productions = {}
        for prod in cfg.productions:
            productions.setdefault(prod.head, [])
        for prod in cfg.productions:
            p = prod.body
            if not p:
                p = [Variable("$")]
            productions[prod.head].append(
                reduce(Regex.concatenate, map(lambda x: Regex(x.value), p))
            )
        prods = {}
        for n, p in productions.items():
            prods[n] = reduce(Regex.union, p)
        return ECFG(variables, terminals, start_symbol, prods)

    @staticmethod
    def from_file(name_file: str, start_sym: Variable = Variable("S")):
        return ECFG.from_cfg(read_cfg_from_file(name_file, start_sym))

    @staticmethod
    def from_str(text: str, start_sym: Variable = Variable("S")):
        return ECFG.from_cfg(CFG.from_text(text, start_sym))


S = Variable("S")
A = Variable("A")
B = Variable("B")
a = Terminal("a")
b = Terminal("b")
prods = []
prods.append(Production(S, [A, S, A]))
prods.append(Production(S, [a, B]))
prods.append(Production(A, [B]))
prods.append(Production(A, [S]))
prods.append(Production(B, [b]))
prods.append(Production(B, [Epsilon()]))
cfg = CFG(
    {S, A, B},
    {a, b},
    S,
    set(prods),
)
f = ECFG.from_cfg(cfg)
rsm = f.to_rsm()
