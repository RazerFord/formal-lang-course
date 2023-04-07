from pyformlang.finite_automaton.finite_automaton import to_symbol, Symbol


class RSM:
    def __init__(self, start_label: Symbol, boxes) -> None:
        self._start_label = to_symbol(start_label) or Symbol("")
        self._boxes = boxes

    @property
    def boxes(self):
        return self._boxes

    @property
    def start_label(self):
        return self._start_label
