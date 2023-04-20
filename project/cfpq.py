import networkx as nx
from pyformlang import cfg
from project.hellings import hellings


def cfpq_hellings(
    graph: nx.MultiGraph | str,
    cfgr: cfg.CFG | str,
    variable: cfg.Variable = None,
    start_nodes: set = None,
    final_nodes: set = None,
) -> set[tuple[int, int]]:
    """
    Parameters
    ----------
        graph: nx.MultiGraph
            The graph in which the reachability is checked
        cfgr: cfg.CFG
            Context-free grammar for graph query
        variable: cfg.Variable
            Start variable in CFG
        start_nodes: set
            Starting vertices in a graph
        final_nodes: set
            Final vertices in a graph

    Returns
    ----------
        set[tuple[int, int]]
            Returns a set of tuples. The first element of the tuple
            is the starting node, the second element of the tuple
            is the final node
    """
    result = hellings(graph, cfgr)
    if start_nodes is None:
        start_nodes = graph.nodes
    if final_nodes is None:
        final_nodes = graph.nodes
    if variable is None:
        variable = cfgr.start_symbol
    answer = set()
    for u, var, v in result:
        if var == variable and u in start_nodes and v in final_nodes:
            answer.add((u, v))
    return answer
