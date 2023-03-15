import scipy.sparse as sp
import numpy as np
import pyformlang.finite_automaton as fa
import networkx as nx
from pyformlang.regular_expression import Regex
from graph_info import parse_labels
from intersection_finite_automata import Mapping


def get_reachable_vertices(
    graph: nx.MultiDiGraph,
    automata: fa.DeterministicFiniteAutomaton,
    start_nodes: list[int],
):
    labels_gr = parse_labels(graph)
    labels_fa = automata.symbols

    matrix_fa, mp_fa = get_boolean_decomposition_and_map_for_fa(labels_fa, automata)
    matrix_gr, mp_gr = get_boolean_decomposition_and_map_for_graph(labels_gr, graph)
    labels = labels_fa.intersection(labels_gr)
    l = list(labels)[0]
    matrices = combine_matrix(matrix_fa, matrix_gr, labels)
    matrix_transition = init_matrix_transition(matrix_fa[l], matrix_gr[l])
    offset, _ = matrix_transition.shape
    mp = mp_fa.get_map()

    prev = matrix_transition.copy()
    for start in automata.start_states:
        indx = mp[start]
        for node in start_nodes:
            matrix_transition[indx, node + offset] = 1

    while not identical_matrices(prev, matrix_transition):
        prev = matrix_transition.copy()
        next_matrices = {}

        for l in labels:
            next_matrices[l] = matrix_transition @ matrices[l]
        matrix_transition = sp.lil_matrix(prev.shape, dtype=int)

        for l in labels:
            n, m = next_matrices[l].shape
            for i in range(n):
                k = i
                for j in range(n):
                    if next_matrices[l][i, j] == 1:
                        k = j
                for j in range(m):
                    matrix_transition[k, j] |= bool(next_matrices[l][i, j])


def identical_matrices(matrix_fst: sp.lil_matrix, matrix_snd: sp.lil_matrix):
    return np.sum(np.logical_xor(matrix_fst.toarray(), matrix_snd.toarray())) == 0


def combine_matrix(
    matrix_fa: dict[str, sp.lil_matrix],
    matrix_gr: dict[str, sp.lil_matrix],
    labels: set,
) -> dict[str, sp.lil_matrix]:
    matrices = {}
    for l in labels:
        number_rows_fa, number_colmn_fa = matrix_fa[l].shape
        number_rows_gr, number_colmn_gr = matrix_gr[l].shape
        add_to_fa = sp.lil_matrix((number_rows_fa, number_colmn_gr), dtype=int)
        add_to_gr = sp.lil_matrix((number_rows_gr, number_colmn_fa), dtype=int)
        add_matrix_fa = sp.hstack([matrix_fa[l], add_to_fa])
        add_matrix_gr = sp.hstack([add_to_gr, matrix_gr[l]])
        matrices[l] = sp.vstack([add_matrix_fa, add_matrix_gr])
    return matrices


def init_matrix_transition(
    matrix_fa: sp.lil_matrix, matrix_gr: sp.lil_matrix
) -> dict[str, sp.lil_matrix]:
    number_rows_fa, _ = matrix_fa.shape
    _, number_colmn_gr = matrix_gr.shape
    i_matrix = sp.lil_matrix(sp.eye(number_rows_fa))
    matrix = sp.lil_matrix(
        sp.hstack(
            [i_matrix, sp.lil_matrix((number_rows_fa, number_colmn_gr), dtype=int)]
        )
    )
    return matrix


def get_boolean_decomposition_and_map_for_graph(
    symbols: set, graph: nx.MultiDiGraph
) -> tuple[dict[str, sp.lil_matrix], Mapping]:
    decomposition, mapp = init_mapping_and_matrix(symbols, sorted(graph.nodes))

    mp = mapp.get_map()
    for u, v, ddict in graph.edges(data=True):
        label = ddict.get("label", None)
        if label is not None:
            decomposition[label][mp[u], mp[v]] = 1

    return decomposition, mapp


def get_boolean_decomposition_and_map_for_fa(
    symbols: set, automata: fa.DeterministicFiniteAutomaton
) -> tuple[dict[str, sp.lil_matrix], Mapping]:
    decomposition, mapp = init_mapping_and_matrix(symbols, list(automata.states))

    mp = mapp.get_map()
    for u, l, v in automata:
        decomposition[l.value][mp[u.value], mp[v.value]] = 1

    return decomposition, mapp


def init_mapping_and_matrix(
    symbols: list, labels: list
) -> tuple[dict[str, sp.lil_matrix], Mapping]:
    decomposition = {}
    number_labels = len(labels)

    for label in symbols:
        decomposition[label] = sp.lil_matrix((number_labels, number_labels), dtype=int)
    mp = Mapping(labels)

    return decomposition, mp


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
    gr.add_transition(0, "b", 0)
    gr.add_transition(0, "a", 1)
    gr.add_transition(1, "b", 2)
    return gr


gr = init_graph()
rx = init_regex()
# print(gr.nodes())
# print(list(rx.states))
# mx = get_boolean_decomposition_and_map_for_fa(rx.symbols, rx)
# print(mx[0]["a"].toarray())
# mx = get_boolean_decomposition_and_map_for_graph(parse_labels(gr), gr)
# print(mx[0]["a"].toarray())
# print(mx[0]['b'].toarray())

get_reachable_vertices(gr, rx, [0])
