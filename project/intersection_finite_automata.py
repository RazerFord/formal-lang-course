import scipy.sparse as sp
import project.finite_automata as fa
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
        self.states = list(states)
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


def get_intersection_two_finite_automata(
    fst_automata: DeterministicFiniteAutomaton,
    snd_automata: DeterministicFiniteAutomaton,
):
    enfa = EpsilonNFA()

    start_states = get_intersection_states(
        fst_automata.start_states, snd_automata.start_states
    )
    for start_state in start_states:
        for state in start_state:
            enfa.add_start_state(state)

    final_states = get_intersection_states(
        fst_automata.final_states, snd_automata.final_states
    )
    for final_state in final_states:
        for state in final_state:
            enfa.add_final_state(state)

    symbols = set(list(fst_automata.symbols) + list(snd_automata.symbols))

    fst_decomposition, fst_map = get_boolean_decomposition_and_map(
        fst_automata, symbols
    )
    snd_decomposition, snd_map = get_boolean_decomposition_and_map(
        snd_automata, symbols
    )

    mtrxes = {}
    for symbol in symbols:
        mtrxes[symbol] = sp.kron(fst_decomposition[symbol], snd_decomposition[symbol])

    num = len(snd_automata.states)
    fst_imp = fst_map.get_imap()
    snd_imp = snd_map.get_imap()
    for key, mtrx in mtrxes.items():
        for i, row in enumerate(mtrx.toarray()):
            for j, val in enumerate(row):
                if val == True:
                    fr = combine_state_pair(
                        State(fst_imp[i // num]), State(snd_imp[i % num])
                    )
                    to = combine_state_pair(
                        State(fst_imp[j // num]), State(snd_imp[j % num])
                    )
                    enfa.add_transition(fr, key, to)
    return enfa


def combine_state_pair(fst_state: State, snd_state: State) -> State:
    return State(str(fst_state.value) + "; " + str(snd_state.value))


def get_intersection_states(
    fst_states: list[State], snd_states: list[State]
) -> list[list[State]]:
    mtrx = []
    for i, fst in enumerate(fst_states):
        mtrx.append([])
        for snd in snd_states:
            mtrx[i].append(combine_state_pair(fst, snd))
    return mtrx


def states_to_list_int(states: list[int]) -> list[int]:
    return [x.value for x in list(states)]


def get_boolean_decomposition_and_map(
    automata: DeterministicFiniteAutomaton, symbols: set
) -> tuple[dict[str, sp.lil_matrix], Mapping]:
    decomposition = {}
    number_states = len(automata.states)

    for label in symbols:
        decomposition[label] = sp.lil_matrix((number_states, number_states), dtype=int)

    mapp = Mapping(automata.states)
    mp = mapp.get_map()

    for u, l, v in automata:
        decomposition[l.value][mp[u.value], mp[v.value]] = 1

    return decomposition, mapp


def regular_query_to_graph(
    regex_expr: str,
    graph: nx.MultiDiGraph,
    start_nodes: list = None,
    final_nodes: list = None,
) -> list[tuple[State, State]]:
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
