import scipy.sparse as sp
import pyformlang.finite_automaton as fa
import networkx as nx
from pyformlang.regular_expression import Regex
from graph_info import parse_labels
from intersection_finite_automata import Mapping


def get_reachable_vertices(
    graph: nx.MultiDiGraph, automata: fa.DeterministicFiniteAutomaton
):
    labels_gr = parse_labels(graph)
    labels_fa = automata.symbols

    matrix_fa, mapp = get_boolean_decomposition_and_map_for_fa(labels_fa, automata)
    matrix_gr, _ = get_boolean_decomposition_and_map_for_graph(labels_gr, gr)
    ...


def get_boolean_decomposition_and_map_for_fa(
    symbols: set, automata: fa.DeterministicFiniteAutomaton
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

def get_boolean_decomposition_and_map_for_graph(
    symbols: set, automata: fa.DeterministicFiniteAutomaton
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

def get_boolean_decomposition_and_map(symbols: list, labels: list):
    decomposition = {}
    number_labels = len(labels)

    for label in symbols:
        decomposition[label] = sp.lil_matrix((number_states, number_states), dtype=int)

    mapp = Mapping(automata.states)
    mp = mapp.get_map()
    ...

def init_graph():
    gr = nx.MultiDiGraph()
    gr.add_edge(0, 3, label="b")
    gr.add_edge(3, 0, label="b")
    gr.add_edge(0, 1, label="a")
    gr.add_edge(1, 2, label="b")
    gr.add_edge(2, 0, label="a")
    return gr

def init_regex():
    gr = fa.DeterministicFiniteAutomaton()
    gr.add_start_state(0)
    gr.add_final_state(2)
    gr.add_transition(0, 'b', 0)
    gr.add_transition(0, 'a', 1)
    gr.add_transition(1, 'b', 2)
    return gr

gr = init_graph()
rx = init_regex()
mx = get_boolean_decomposition_and_map_for_fa(rx.symbols, rx)
print(mx[0]['b'].toarray())
get_reachable_vertices(gr, rx)