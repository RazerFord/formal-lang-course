import scipy.sparse as sp
from networkx import MultiDiGraph
from finite_automata import create_non_deterministic_automaton_from_graph
from pyformlang.finite_automaton import DeterministicFiniteAutomaton
from graph_info import parse_labels
from numpy import array


def get_intersection_two_finite_automata(
    fst_automata: DeterministicFiniteAutomaton,
    snd_automata: DeterministicFiniteAutomaton,
):
    fst_decomposition = get_boolean_decomposition(fst_automata)
    snd_decomposition = get_boolean_decomposition(snd_automata)


def get_boolean_decomposition(automata: DeterministicFiniteAutomaton):
    graph = automata.to_networkx()
    decomposition = {}

    number_nodes = graph.number_of_nodes()

    labels = parse_labels(graph)

    for label in labels:
        decomposition[label] = sp.lil_matrix((number_nodes, number_nodes), dtype=int)

    for u, v, ddict in graph.edges(data=True):
        label = ddict.get("label", None)
        if label is not None:
            decomposition[label][u][v] = 1

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
get_intersection_two_finite_automata(enfa_db, enfa_query)

# obj = enfa_db.get_intersection(enfa_query)
# print(obj.start_states)
# print(obj.final_states)
# print(obj.to_networkx().edges(data=True))
# print()
# print(obj.to_networkx().nodes())
