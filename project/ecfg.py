from pyformlang.cfg import Production, Variable, Terminal, CFG, Epsilon
from pyformlang.cfg.utils import to_variable, to_terminal
from pyformlang.regular_expression import Regex
from pyformlang.finite_automaton.finite_automaton import to_symbol
from project.context_free_grammar import read_cfg_from_file
from project.rsm import RSM
from functools import reduce
from typing import AbstractSet, Iterable


class ECFG:
    """
    Class of extended context-free grammars

    Parameters
    ----------
    variables : AbstractSet[Variable]
        Set of variables in ECFG
    terminals : AbstractSet
        Set of terminals in ECFG
    start_symbol : Variable
        Start symbol of ECFG
    productions : Iterable[Production]
        Productions of ECFG
    """

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
    def productions(self) -> Iterable[Production]:
        """
        Parameters
        ----------

        Returns
        ----------
        Iterable[Production]
            Returns productions
        """
        return self._productions

    @property
    def start_symbol(self) -> Variable:
        """
        Parameters
        ----------

        Returns
        ----------
        Variable
            Returns start symbol
        """
        return self._start_symbol

    @property
    def terminals(self) -> AbstractSet[Terminal]:
        """
        Parameters
        ----------

        Returns
        ----------
        AbstractSet[Terminal]
            Returns set of terminals
        """
        return self._terminals

    @property
    def variables(self) -> AbstractSet[Variable]:
        """
        Parameters
        ----------

        Returns
        ----------
        AbstractSet[Terminal]
            Returns set of variables
        """
        return self._variables

    def to_rsm(self) -> RSM:
        """
        Parameters
        ----------

        Returns
        ----------
        RSM
            Returns RSM, which is derived from ECFG
        """
        boxes = {
            to_symbol(n.value): p.to_epsilon_nfa() for n, p in self._productions.items()
        }
        s = to_symbol(self._start_symbol.value)
        return RSM(s, boxes)

    @staticmethod
    def from_cfg(cfg: CFG) -> "ECFG":
        """
        Parameters
        ----------
        cfg : CFG
            CFG from which ECFG is produced

        Returns
        ----------
        RSM
            Returns ECFG from CFG
        """
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
    def from_file(name_file: str, start_sym: Variable = Variable("S")) -> "ECFG":
        """
        Parameters
        ----------
        name_file : str
            The name of the file from which the CFG is read
        start_sym :
            Start symbol
        Returns
        ----------
        RSM
            Returns ECFG from file
        """
        return ECFG.from_cfg(read_cfg_from_file(name_file, start_sym))

    @staticmethod
    def from_str(text: str, start_sym: Variable = Variable("S")) -> "ECFG":
        """
        Parameters
        ----------
        text : str
            The strign from which the CFG is read
        start_sym :
            Start symbol
        Returns
        ----------
        RSM
            Returns ECFG from string
        """
        return ECFG.from_cfg(CFG.from_text(text, start_sym))
