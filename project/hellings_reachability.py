import networkx as nx
from pyformlang import cfg
from context_free_grammar import cfg_to_wcnf


def hellings(graph: nx.MultiGraph, cfgr: cfg.CFG):
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
    print(result)


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


S = cfg.Variable("S")
S1 = cfg.Variable("S1")
B = cfg.Variable("B")
A = cfg.Variable("A")
a = cfg.Terminal("a")
b = cfg.Terminal("b")
prods = []
prods.append(cfg.Production(S, [A, B]))
prods.append(cfg.Production(S, [A, S1]))
prods.append(cfg.Production(S1, [S, B]))
prods.append(cfg.Production(A, [a]))
prods.append(cfg.Production(B, [b]))
test_cfg = cfg.CFG(
    variables={S, A, B, S1},
    terminals={a, b},
    start_symbol=S,
    productions=set(prods),
)

graph = nx.MultiDiGraph()
graph.add_edge(0, 1, label="a")
graph.add_edge(1, 2, label="a")
graph.add_edge(2, 0, label="a")
graph.add_edge(2, 3, label="b")
graph.add_edge(3, 2, label="b")
hellings(graph, test_cfg)
