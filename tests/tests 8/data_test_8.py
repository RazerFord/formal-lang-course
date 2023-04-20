from pyformlang import cfg
import networkx as nx


def cfg_simple():
    S = cfg.Variable("S")
    B = cfg.Variable("B")
    A = cfg.Variable("A")
    a = cfg.Terminal("a")
    b = cfg.Terminal("b")
    prods = []
    prods.append(cfg.Production(S, [A, B]))
    prods.append(cfg.Production(A, [a]))
    prods.append(cfg.Production(B, [b]))
    prods.append(cfg.Production(A, [cfg.Epsilon()]))
    return cfg.CFG(
        variables={S, A, B},
        terminals={a, b},
        start_symbol=S,
        productions=set(prods),
    )


def graph_simple():
    graph = nx.MultiDiGraph()
    graph.add_edge(0, 1, label="a")
    graph.add_edge(1, 2, label="b")
    return graph


def answer_simple():
    S = cfg.Variable("S")
    B = cfg.Variable("B")
    A = cfg.Variable("A")
    return set(
        [
            (0, A, 1),
            (1, B, 2),
            (0, S, 2),
            (1, S, 2),
            (0, A, 0),
            (1, A, 1),
            (2, A, 2),
        ]
    )


def cfg_hard():
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
    return cfg.CFG(
        variables={S, A, B, S1},
        terminals={a, b},
        start_symbol=S,
        productions=set(prods),
    )


def graph_hard():
    graph = nx.MultiDiGraph()
    graph.add_edge(0, 1, label="a")
    graph.add_edge(1, 2, label="a")
    graph.add_edge(2, 0, label="a")
    graph.add_edge(2, 3, label="b")
    graph.add_edge(3, 2, label="b")
    return graph


def answer_hard():
    S = cfg.Variable("S")
    S1 = cfg.Variable("S1")
    B = cfg.Variable("B")
    A = cfg.Variable("A")
    return set(
        [
            (0, A, 1),
            (1, A, 2),
            (2, A, 0),
            (2, B, 3),
            (3, B, 2),
            (1, S, 3),
            (1, S1, 2),
            (0, S, 2),
            (0, S1, 3),
            (2, S, 3),
            (2, S1, 2),
            (1, S, 2),
            (1, S1, 3),
            (0, S, 3),
            (0, S1, 2),
            (2, S, 2),
            (2, S1, 3),
        ]
    )
