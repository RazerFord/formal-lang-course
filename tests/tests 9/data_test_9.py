from pyformlang import cfg
import networkx as nx


def cfg_first_hard():
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


def cfg_second_hard():
    S = cfg.Variable("S")
    B = cfg.Variable("B")
    A = cfg.Variable("A")
    a = cfg.Terminal("a")
    b = cfg.Terminal("b")
    prods = []
    prods.append(cfg.Production(S, [A, B]))
    prods.append(cfg.Production(A, [a]))
    prods.append(cfg.Production(B, [b]))
    return cfg.CFG(
        variables={S, A, B},
        terminals={a, b},
        start_symbol=S,
        productions=set(prods),
    )


def graph_hard():
    graph = nx.MultiDiGraph()
    graph.add_edge(0, 1, label="a")
    graph.add_edge(1, 2, label="a")
    graph.add_edge(2, 0, label="a")
    graph.add_edge(3, 0, label="b")
    graph.add_edge(0, 3, label="b")
    return graph


def answer_hard_first():
    S = cfg.Variable("S")
    S1 = cfg.Variable("S1")
    B = cfg.Variable("B")
    A = cfg.Variable("A")
    return set(
        [
            (0, S1, 0),
            (0, S, 0),
            (0, A, 1),
            (0, B, 3),
            (0, S, 3),
            (0, S1, 3),
            (1, S, 0),
            (1, S1, 0),
            (1, A, 2),
            (1, S1, 3),
            (1, S, 3),
            (2, A, 0),
            (2, S1, 0),
            (2, S, 0),
            (2, S, 3),
            (2, S1, 3),
            (3, B, 0),
        ]
    )


def answer_hard_second():
    S = cfg.Variable("S")
    B = cfg.Variable("B")
    A = cfg.Variable("A")
    return set(
        [
            (0, A, 1),
            (2, S, 3),
            (1, A, 2),
            (0, B, 3),
            (3, B, 0),
            (2, A, 0),
        ]
    )
