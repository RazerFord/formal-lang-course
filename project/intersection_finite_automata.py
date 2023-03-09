import scipy.sparse as sp
from networkx import MultiDiGraph
from finite_automata import create_non_deterministic_automaton_from_graph
from pyformlang.finite_automaton import DeterministicFiniteAutomaton
from pyformlang.finite_automaton import State, EpsilonNFA


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

    fst_decomposition = get_boolean_decomposition(fst_automata, symbols)
    snd_decomposition = get_boolean_decomposition(snd_automata, symbols)

    mtrxes = {}
    for symbol in symbols:
        mtrxes[symbol] = sp.kron(fst_decomposition[symbol], snd_decomposition[symbol])

    for key, mtrx in mtrxes.items():
        for i, row in enumerate(mtrx.toarray()):
            for j, val in enumerate(row):
                if val == True:
                    enfa.add_transition(i, key, j)

    return enfa


def get_intersection_states(fst_states: list[State], snd_states: list[State]):
    mtrx = []
    for i, fst in enumerate(fst_states):
        mtrx.append([])
        for snd in snd_states:
            mtrx[i].append(combine_state_pair(fst, snd))
    return mtrx


def combine_state_pair(fst_state, snd_state):
    return State(str(fst_state.value) + "; " + str(snd_state.value))


def states_to_list_int(states: list[int]):
    return [x.value for x in list(states)]


def get_boolean_decomposition(automata: DeterministicFiniteAutomaton, symbols: set):
    decomposition = {}
    number_states = len(automata.states)

    for label in symbols:
        decomposition[label] = sp.lil_matrix((number_states, number_states), dtype=int)

    for u, l, v in automata:
        decomposition[l.value][u.value, v.value] = 1

    return decomposition


def create_dfa_db():
    gr = MultiDiGraph()
    start_nodes = [0, 1]
    final_nodes = [1, 0]
    labels = ["a", "b"]

    for u, v, l in zip(start_nodes, final_nodes, labels):
        gr.add_edge(u, v, label=l)
    enfa = create_non_deterministic_automaton_from_graph(gr, start_nodes, final_nodes)
    return enfa


def create_dfa_query():
    gr = MultiDiGraph()
    start_nodes = [0, 0]
    final_nodes = [0, 0]
    labels = ["a", "b"]

    for u, v, l in zip(start_nodes, final_nodes, labels):
        gr.add_edge(u, v, label=l)
    enfa = create_non_deterministic_automaton_from_graph(
        gr, list(set(start_nodes)), list(set(final_nodes))
    )
    return enfa


enfa_db = create_dfa_db()
enfa_query = create_dfa_query()
jjj = get_intersection_two_finite_automata(enfa_db, enfa_query)

obj = enfa_db.get_intersection(enfa_query)
print(jjj.to_networkx().edges(data=True))
print(obj.to_networkx().edges(data=True))
# print(obj.final_states)
# print()
# print(obj.to_networkx().nodes())
