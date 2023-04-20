import networkx as nx
from pathlib import Path
from pyformlang import cfg
from project.context_free_grammar import cfg_to_wcnf
from project.context_free_grammar import read_cfg_from_file


def hellings(
    graph: nx.MultiGraph | str, cfgr: cfg.CFG | str
) -> set[tuple[int, cfg.Variable, int]]:
    """
    Parameters
    ----------
        graph: nx.MultiGraph
            The graph or path to the graph for which the reachability is
            being checked
        cfgr: cfg.CFG
            Context-free grammar or the path to the file in which it is
            stored

    Returns
    ----------
        set[tuple[int, cfg.Variable, int]]
            Returns a set of tuples. The first element of the tuple
            is the start symbol, the second element is the non-terminal
            symbol, the third is the final node
    """
    if isinstance(graph, str):
        graph = (
            nx.adjlist.read_adjlist(graph, create_using=nx.MultiDiGraph, nodetype=int),
        )
    if isinstance(cfgr, str) and Path(cfgr).is_file():
        cfgr = read_cfg_from_file(cfgr)
    if isinstance(cfgr, str) and not Path(cfgr).is_file():
        cfgr = cfg.CFG.from_text(cfgr)
    wcnf = cfg_to_wcnf(cfgr)
    graph = _init_new_graph(graph, wcnf)
    result = set()
    queue = list()
    for u, v, l in graph.edges.data(data="label"):
        queue.append((u, l, v))
        result.add((u, l, v))
    while len(queue) != 0:
        u, var, v = queue.pop(0)
        add = set()
        for un, varn, vn in result:
            if u == vn:
                for prod in wcnf.productions:
                    p = un, prod.head, v
                    if [varn, var] == prod.body and p not in result:
                        queue.append(p)
                        add.add(p)
        for un, varn, vn in result:
            if v == un:
                for prod in wcnf.productions:
                    p = u, prod.head, vn
                    if [var, varn] == prod.body and p not in result:
                        queue.append(p)
                        add.add(p)
        result = result.union(add)
    return result


def _init_new_graph(graph: nx.MultiGraph, wcnf: cfg.CFG) -> nx.MultiGraph:
    new_graph = nx.MultiDiGraph()
    terminal_to_variable = {}
    variables = set()
    for prod in wcnf.productions:
        if len(prod.body) == 1 and isinstance(prod.body[0], cfg.Terminal):
            terminal_to_variable[prod.body[0]] = prod.head
        if len(prod.body) == 0:
            variables.add(prod.head)
    for u, v, l in graph.edges.data(data="label"):
        var = terminal_to_variable[cfg.Terminal(l)]
        new_graph.add_edge(u, v, label=var)
    for node in new_graph.nodes:
        for var in variables:
            new_graph.add_edge(node, node, label=var)
    return new_graph
