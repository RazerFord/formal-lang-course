import scipy.sparse as sp
import numpy as np
import pyformlang.finite_automaton as fa
import networkx as nx
from project.graph_info import parse_labels
from project.intersection_finite_automata import Mapping
from project.finite_automata import create_deterministic_automaton_from_regex


def get_reachable_vertices(
    graph: nx.MultiDiGraph,
    automata: fa.DeterministicFiniteAutomaton,
    start_nodes: list,
):
    number_start_nodes = len(start_nodes)
    if number_start_nodes > len(graph.nodes):
        raise ValueError("Fail number of starting vertices")
    labels_gr = parse_labels(graph)
    labels_fa = automata.symbols
    matrix_fa, mp_fa = _get_boolean_decomposition_and_map_for_fa(labels_fa, automata)
    matrix_gr, mp_gr = _get_boolean_decomposition_and_map_for_graph(labels_gr, graph)
    labels = labels_fa.intersection(labels_gr)
    l = list(labels)[0]
    matrices = _combine_matrix(matrix_fa, matrix_gr, labels)
    matrix_transition, offset, length = _init_start_matrix(
        matrix_fa[l].shape[0],
        matrix_gr[l].shape[1],
        start_nodes,
        automata.start_states,
        mp_fa,
        mp_gr,
    )
    matrix_result = _do_bfs(
        matrix_transition,
        matrices,
        matrix_fa[l].shape[0],
        matrix_gr[l].shape[1],
        number_start_nodes,
    )
    mp_fa_to_indx = mp_fa.get_map()
    mp_to_node = mp_gr.get_imap()
    res_u_v = set()
    for k, v in enumerate(start_nodes):
        for final in automata.final_states:
            indx = mp_fa_to_indx[final]
            for i in range(offset, length, 1):
                if matrix_result[indx + k * offset, i]:
                    res_u_v.add((v, mp_to_node[i - offset]))
    return res_u_v


def _do_bfs(
    matrix_transition: sp.lil_matrix,
    matrices: sp.lil_matrix,
    offset: int,
    length: int,
    number_starts: int,
) -> np.array:
    count_non_zeros = -1
    visibles = matrix_transition.copy()
    start_matrix = matrix_transition.copy()
    while visibles.count_nonzero() != count_non_zeros:
        count_non_zeros = visibles.count_nonzero()
        t_matrix = _init_matrix_transition(offset, length, number_starts)
        for matrix in matrices.values():
            n_matrix = matrix_transition @ matrix
            for k in range(number_starts):
                for i in range(offset):
                    for j in range(offset):
                        if n_matrix[i + offset * k, j]:
                            t_matrix[j + offset * k, offset:] += n_matrix[
                                i + offset * k, offset:
                            ]
        matrix_transition = t_matrix
        visibles += t_matrix
    return np.logical_xor(visibles.toarray(), start_matrix.toarray())


def _combine_matrix(
    matrix_fa: dict[str, sp.lil_matrix],
    matrix_gr: dict[str, sp.lil_matrix],
    labels: set,
) -> dict[str, sp.lil_matrix]:
    matrices = {}
    for l in labels:
        number_rows_fa, number_colmn_fa = matrix_fa[l].shape
        number_rows_gr, number_colmn_gr = matrix_gr[l].shape
        add_to_fa = sp.lil_matrix((number_rows_fa, number_colmn_gr), dtype=bool)
        add_to_gr = sp.lil_matrix((number_rows_gr, number_colmn_fa), dtype=bool)
        add_matrix_fa = sp.hstack([matrix_fa[l], add_to_fa])
        add_matrix_gr = sp.hstack([add_to_gr, matrix_gr[l]])
        matrices[l] = sp.vstack([add_matrix_fa, add_matrix_gr])
    return matrices


def _init_start_matrix(
    number_rows_fa: int,
    number_colmn_gr: int,
    start_nodes: list,
    start_states: list,
    mp_fa: Mapping,
    mp_gr: Mapping,
) -> tuple[sp.lil_matrix, int, int]:
    matrix_transition = _init_matrix_transition(
        number_rows_fa, number_colmn_gr, len(start_nodes)
    )
    offset, length = matrix_transition.shape
    offset = offset // len(start_nodes)
    mp_fa_to_indx = mp_fa.get_map()
    mp_gr_to_indx = mp_gr.get_map()

    for start in start_states:
        indx = mp_fa_to_indx[start]
        for i, node in enumerate(start_nodes):
            indx_node = mp_gr_to_indx[node]
            matrix_transition[indx + i * offset, indx_node + offset] = 1
    return matrix_transition, offset, length


def _init_matrix_transition(
    number_rows_fa: int, number_colmn_gr: int, n: int
) -> sp.lil_matrix:
    template = sp.lil_matrix(
        sp.eye(
            number_rows_fa, number_rows_fa + number_colmn_gr, dtype=bool, format="lil"
        )
    )
    matrix = template
    for _ in range(n - 1):
        matrix = sp.lil_matrix(sp.vstack([matrix, template]), dtype=bool)
    return matrix


def _get_boolean_decomposition_and_map_for_graph(
    symbols: set, graph: nx.MultiDiGraph
) -> tuple[dict[str, sp.lil_matrix], Mapping]:
    decomposition, mapp = _init_mapping_and_matrix(symbols, sorted(graph.nodes))

    mp = mapp.get_map()
    for u, v, ddict in graph.edges(data=True):
        label = ddict.get("label", None)
        if label is not None:
            decomposition[label][mp[u], mp[v]] = 1

    return decomposition, mapp


def _get_boolean_decomposition_and_map_for_fa(
    symbols: set, automata: fa.DeterministicFiniteAutomaton
) -> tuple[dict[str, sp.lil_matrix], Mapping]:
    decomposition, mapp = _init_mapping_and_matrix(symbols, list(automata.states))

    mp = mapp.get_map()
    for u, l, v in automata:
        decomposition[l.value][mp[u.value], mp[v.value]] = 1

    return decomposition, mapp


def _init_mapping_and_matrix(
    symbols: list, labels: list
) -> tuple[dict[str, sp.lil_matrix], Mapping]:
    decomposition = {}
    number_labels = len(labels)

    for label in symbols:
        decomposition[label] = sp.lil_matrix((number_labels, number_labels), dtype=bool)
    mp = Mapping(labels)

    return decomposition, mp


def _do_query(
    func,
    graph: nx.MultiDiGraph,
    regex_expr: str,
    start_nodes: list,
    final_nodes: list = None,
):
    if final_nodes is None:
        final_nodes = graph.nodes()
    regex = create_deterministic_automaton_from_regex(regex_expr)
    res_u_v = get_reachable_vertices(graph, regex, start_nodes)
    new_res_u_v = set()
    for u, v in res_u_v:
        if v in final_nodes:
            new_res_u_v.add(func(u, v))
    return new_res_u_v


def regular_query_to_graph_each(
    graph: nx.MultiDiGraph, regex_expr: str, start_nodes: list, final_nodes: list = None
) -> set:
    func = lambda x, y: (x, y)
    return _do_query(func, graph, regex_expr, start_nodes, final_nodes)


def regular_query_to_graph_all(
    graph: nx.MultiDiGraph, regex_expr: str, start_nodes: list, final_nodes: list = None
) -> set:
    func = lambda _, y: y
    return _do_query(func, graph, regex_expr, start_nodes, final_nodes)
