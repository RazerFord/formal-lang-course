import networkx as nx
import scipy.sparse as sp
from pyformlang import cfg
from pathlib import Path
from project.context_free_grammar import cfg_to_wcnf
from project.context_free_grammar import read_cfg_from_file
from project.intersection_finite_automata import Mapping


def matrix(
    graph: nx.MultiGraph | str, cfgr: cfg.CFG | str
) -> set[tuple[int, cfg.Variable, int]]:
    if isinstance(graph, str):
        graph = (
            nx.adjlist.read_adjlist(graph, create_using=nx.MultiDiGraph, nodetype=int),
        )
    if isinstance(cfgr, str) and Path(cfgr).is_file():
        cfgr = read_cfg_from_file(cfgr)
    if isinstance(cfgr, str) and not Path(cfgr).is_file():
        cfgr = cfg.CFG.from_text(cfgr)

    wcnf = cfg_to_wcnf(cfgr)
    matrices, mp = _init_matrix(graph, wcnf)

    active_productions = set([p for p in wcnf.productions if len(p.body) == 2])

    changed = True
    while changed:
        changed = False
        for p in active_productions:
            nonzero = matrices[p.head].count_nonzero()
            matrices[p.head] += matrices[p.body[0]] @ matrices[p.body[1]]
            changed |= nonzero != matrices[p.head].count_nonzero()

    imp = mp.get_imap()
    ans = set()
    for p in wcnf.productions:
        for u, v in zip(*matrices[p.head].nonzero()):
            ans.add((imp[u], p.head, imp[v]))
    return ans


def _init_matrix(graph: nx.MultiGraph, wcnf: cfg.CFG) -> tuple[map, Mapping]:
    from_terminals = {
        v.body[0].value: v.head for v in wcnf.productions if len(v.body) == 1
    }
    n = graph.number_of_nodes()
    edges = {}
    for _, _, l in graph.edges.data(data="label"):
        edges[from_terminals[l]] = []
    for u, v, l in graph.edges.data(data="label"):
        edges[from_terminals[l]].append((u, v))
    matrices = {v: sp.lil_matrix((n, n), dtype=bool) for v in wcnf.variables}

    mp = Mapping(graph.nodes)
    mpp = mp.get_map()
    for k, v in matrices.items():
        if k in edges:
            for fr, to in edges[k]:
                v[mpp[fr], mpp[to]] = True

    prod_eps = [p.head for p in wcnf.productions if len(p.body) == 0]
    for k in prod_eps:
        for i in range(n):
            matrices[k][i, i] = True

    return matrices, mp
