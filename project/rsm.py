from pyformlang.finite_automaton.finite_automaton import to_symbol, Symbol
from pyformlang.finite_automaton import EpsilonNFA
import scipy.sparse as sp
from project.intersection_finite_automata import (
    get_boolean_decomposition_and_map,
    Mapping,
)


class RSM:
    """
    Class of recursive state machine

    Parameters
    ----------
    start_label : Symbol
        Start symbol in RSM
    boxes : dict[Symbol, EpsilonNFA]
        Boxes of rules
    """

    def __init__(self, start_label: Symbol, boxes: dict[Symbol, EpsilonNFA]) -> None:
        self._start_label = to_symbol(start_label) or Symbol("")
        self._boxes = boxes

    def minimize(self) -> "RSM":
        """
        Parameters
        ----------

        Returns
        ----------
        RSM
            Returns RMS with minimized of rule in boxes
        """
        for k, v in self.boxes.items():
            self.boxes[k] = v.minimize()
        return self

    @property
    def boxes(self) -> dict[Symbol, EpsilonNFA]:
        """
        Parameters
        ----------

        Returns
        ----------
        dict[Symbol, EpsilonNFA]
            Returns boxes
        """
        return self._boxes

    @property
    def start_label(self) -> Symbol:
        """
        Parameters
        ----------

        Returns
        ----------
        Symbol
            Returns start_label
        """
        return self._start_label

    @property
    def matrices(self) -> dict[tuple[dict[str, sp.lil_matrix], Mapping]]:
        """
        Parameters
        ----------

        Returns
        ----------
        dict[tuple[dict[str, sp.lil_matrix], Mapping]]
            Returns boolean decomposition
        """
        matrices = {}
        for ch, val in self.boxes.items():
            labels = {l.value for _, l, _ in val}
            matrices[ch] = get_boolean_decomposition_and_map(labels, val)
        return matrices

    def to_matrices(self) -> dict[tuple[dict[str, sp.lil_matrix], Mapping]]:
        """
        Parameters
        ----------

        Returns
        ----------
        dict[tuple[dict[str, sp.lil_matrix], Mapping]]
            Returns boolean decomposition
        """
        return self.matrices
