import scipy.sparse as sp
import finite_automata as fa
import networkx as nx
from pyformlang.finite_automaton import DeterministicFiniteAutomaton
from pyformlang.finite_automaton import State
from pyformlang.finite_automaton import EpsilonNFA


class Mapping:
    """
    Creates a dictionary mapping the state value to a
    number from zero, and a dictionary mapping numbers to
    states

    Parameters
    ----------
    states : list[State]
        All states in the graph that is passed to the class
    """

    def __init__(self, states: list[State]):
        self.states = states
        self._mapp, self._invert_mapp = self._init_mapping()

    def _init_mapping(self):
        mapp = {}
        imapp = {}
        for k, state in enumerate(self.states):
            mapp[state] = k
            imapp[k] = state
        return mapp, imapp

    def get_map(self) -> dict[State, int]:
        """
        Parameters
        ----------

        Returns
        ----------
        dict[State, int]
            Returns a dictionary mapping the state value to a number
        """
        return self._mapp

    def get_imap(self) -> dict[int, State]:
        """
        Parameters
        ----------

        Returns
        ----------
        dict[State, int]
            Returns a dictionary representing numbers in states
        """
        return self._invert_mapp


class IntersectionFiniteAutomata:
    """
    Class for finding the intersection of two finite automata

    Parameters
    ----------
    fst_automata : DeterministicFiniteAutomaton
        First deterministic finite automata
    snd_automata : DeterministicFiniteAutomaton
        Second deterministic finite automata
    """

    def __init__(
        self,
        fst_automata: DeterministicFiniteAutomaton,
        snd_automata: DeterministicFiniteAutomaton,
    ):
        self.enfa = EpsilonNFA()
        self._init_states(fst_automata, snd_automata)
        self.symbols = set(list(fst_automata.symbols) + list(snd_automata.symbols))
        self._fst_decompos, self._fst_mp = get_boolean_decomposition_and_map(
            self.symbols, fst_automata
        )
        self._snd_decompos, self._snd_mp = get_boolean_decomposition_and_map(
            self.symbols, snd_automata
        )
        self._mtrxes = self._calculate_kron()
        self._add_transitions(len(snd_automata.states))

    def _init_states(
        self,
        fst_automata: DeterministicFiniteAutomaton,
        snd_automata: DeterministicFiniteAutomaton,
    ):
        start_states = IntersectionFiniteAutomata.get_intersection_states(
            fst_automata.start_states, snd_automata.start_states
        )
        for start_state in start_states:
            for state in start_state:
                self.enfa.add_start_state(state)

        final_states = IntersectionFiniteAutomata.get_intersection_states(
            fst_automata.final_states, snd_automata.final_states
        )
        for final_state in final_states:
            for state in final_state:
                self.enfa.add_final_state(state)

    def _calculate_kron(self):
        mtrxes = {}
        for symbol in self.symbols:
            mtrxes[symbol] = sp.kron(
                self._fst_decompos[symbol], self._snd_decompos[symbol]
            )
        return mtrxes

    def _add_transitions(self, num: int):
        fst_imp = self._fst_mp.get_imap()
        snd_imp = self._snd_mp.get_imap()
        for key, mtrx in self._mtrxes.items():
            for i, row in enumerate(mtrx.toarray()):
                for j, val in enumerate(row):
                    if val == True:
                        fr = IntersectionFiniteAutomata.combine_state_pair(
                            State(fst_imp[i // num]), State(snd_imp[i % num])
                        )
                        to = IntersectionFiniteAutomata.combine_state_pair(
                            State(fst_imp[j // num]), State(snd_imp[j % num])
                        )
                        self.enfa.add_transition(fr, key, to)

    @staticmethod
    def combine_state_pair(fst_state: State, snd_state: State) -> State:
        """
        Parameters
        ----------
        fst_state : State
            State of the first graph
        snd_state : State
            State of the second graph

        Returns
        ----------
        State
            Returns the union of two states into one
        """
        return State(str(fst_state.value) + "; " + str(snd_state.value))

    @staticmethod
    def get_intersection_states(
        fst_states: list[State], snd_states: list[State]
    ) -> list[list[State]]:
        """
        Parameters
        ----------
        fst_states : list[State]
            States of the first graph
        snd_states : list[State]
            States of the second graph

        Returns
        ----------
        list[list[State]]
            Returns a combination of all graph states
        """
        mtrx = []
        for i, fst in enumerate(fst_states):
            mtrx.append([])
            for snd in snd_states:
                mtrx[i].append(IntersectionFiniteAutomata.combine_state_pair(fst, snd))
        return mtrx

    def get_enfa(self) -> EpsilonNFA:
        """
        Returns
        ----------
        EpsilonNFA
            Return NFA
        """
        return self.enfa


def get_boolean_decomposition_and_map(
    symbols: set, automata: DeterministicFiniteAutomaton
) -> tuple[dict[str, sp.lil_matrix], Mapping]:
    """
    Parameters
    ----------
    symbols : set
        Symbols of the automata
    automata : DeterministicFiniteAutomaton
        Automata

    Returns
    ----------
    tuple[dict[str, sp.lil_matrix], Mapping]
        Returns boolean decomposition, map
    """
    decomposition = {}
    number_states = len(automata.states)

    for label in symbols:
        decomposition[label] = sp.lil_matrix((number_states, number_states), dtype=int)

    mapp = Mapping(list(automata.states))
    mp = mapp.get_map()

    for u, l, v in automata:
        decomposition[l.value][mp[u.value], mp[v.value]] = 1

    return decomposition, mapp


def get_intersection_two_finite_automata(
    fst_automata: DeterministicFiniteAutomaton,
    snd_automata: DeterministicFiniteAutomaton,
):
    """
    Parameters
    ----------
    fst_automata : DeterministicFiniteAutomaton
        First deterministic finite automata
    snd_automata : DeterministicFiniteAutomaton
        Second deterministic finite automata

    Returns
    ----------
        Returns the intersection of two finite automata
    """
    intersection = IntersectionFiniteAutomata(fst_automata, snd_automata)
    return intersection.get_enfa()


def regular_query_to_graph(
    regex_expr: str,
    graph: nx.MultiDiGraph,
    start_nodes: list = None,
    final_nodes: list = None,
) -> list[tuple[State, State]]:
    """
    Parameters
    ----------
    regex_expr : str
        Regular expression written as a string
    graph : nx.MultiDiGraph
        The graph from which nfa is built
    start_nodes : list[State]
        List of start nodes
    final_nodes : list[State]
        List of final nodes

    Returns
    ----------
    list[tuple[State, State]]
        Returns a list of pairs such that the first
        element of each pair is reachable from the second
    """
    dfa_from_reg = fa.create_deterministic_automaton_from_regex(regex_expr)
    dfa_from_graph = fa.create_non_deterministic_automaton_from_graph(
        graph, start_nodes, final_nodes
    )
    dfa_intersection = get_intersection_two_finite_automata(
        dfa_from_reg, dfa_from_graph
    )
    pairs = []
    graph = dfa_intersection.to_networkx()
    for start in dfa_intersection.start_states:
        for final in dfa_intersection.final_states:
            if nx.has_path(graph, start, final):
                pairs.append((start.value, final.value))
    return pairs
