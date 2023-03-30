import networkx as nx
from project.reachable_regular_constraints import get_reachable_vertices
from project.finite_automata import create_deterministic_automaton_from_regex


class TestGetReachableVertices:
    def test_query(self):
        regex_expr = "b* a b"
        regex = create_deterministic_automaton_from_regex(regex_expr)
        graph = self.init_graph()
        reachable_vs = get_reachable_vertices(graph, regex, [3, 2, 1])
        pair_vertices = self.reachable_vertices()
        assert reachable_vs == pair_vertices

    def init_graph(self):
        gr = nx.MultiDiGraph()
        gr.add_edge(0, 3, label="b")
        gr.add_edge(3, 0, label="b")
        gr.add_edge(0, 1, label="a")
        gr.add_edge(1, 2, label="b")
        gr.add_edge(3, 2, label="b")
        gr.add_edge(2, 0, label="a")
        return gr

    def reachable_vertices(self):
        return {(2, 3), (3, 2), (3, 3), (1, 3)}
