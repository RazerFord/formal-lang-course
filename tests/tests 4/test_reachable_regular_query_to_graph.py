import networkx as nx
from project.reachable_regular_constraints import regular_query_to_graph_all
from project.reachable_regular_constraints import regular_query_to_graph_each


class TestReachableRegularQueryToGraph:
    def test_query(self):
        regex_expr = "b* a b"
        graph = self.init_graph()
        reachable_vs_each = regular_query_to_graph_each(
            graph, regex_expr, [3, 2, 1, 0], [2, 1]
        )
        reachable_vs_all = regular_query_to_graph_all(
            graph, regex_expr, [3, 2, 1], [2, 1]
        )
        reachable_vertices_each = self.reachable_vertices_each()
        reachable_vertices_all = self.reachable_vertices_all()

        assert reachable_vs_all == reachable_vertices_all
        assert reachable_vs_each == reachable_vertices_each

    def init_graph(self):
        gr = nx.MultiDiGraph()
        gr.add_edge(0, 3, label="b")
        gr.add_edge(3, 0, label="b")
        gr.add_edge(0, 1, label="a")
        gr.add_edge(1, 2, label="b")
        gr.add_edge(3, 2, label="b")
        gr.add_edge(2, 0, label="a")
        return gr

    def reachable_vertices_all(self):
        return {2}

    def reachable_vertices_each(self):
        return {(0, 2), (3, 2)}
