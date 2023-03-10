import networkx as nx
from project.intersection_finite_automata import regular_query_to_graph


class TestRegularQueryToGraph:
    def test_query(self):
        graph, start_nodes, final_nodes = self.init_graph()
        data = regular_query_to_graph(
            "a|b", graph, list(set(start_nodes)), list(set(final_nodes))
        )
        fst, snd = data[0]
        assert (fst[-1], snd[-1]) == ("0", "0")

    def init_graph(self):
        gr = nx.MultiDiGraph()
        start_nodes = [0, 0]
        final_nodes = [0, 0]
        labels = ["a", "b"]
        for u, v, l in zip(start_nodes, final_nodes, labels):
            gr.add_edge(u, v, label=l)
        return gr, list(set(start_nodes)), list(set(final_nodes))
