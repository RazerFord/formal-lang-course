from graph import graph
from networkx import MultiDiGraph
from project.finite_automata import create_non_deterministic_automaton_from_graph
from pyformlang.finite_automaton import Epsilon
import cfpq_data


class TestCreateNonDeterministicAutomatonFromGraph:
    def test_automata_from_graph(self):
        gr = MultiDiGraph()
        start_nodes = graph["start_nodes"]
        final_nodes = graph["final_nodes"]
        labels = graph["labels"]

        for u, v, l in zip(start_nodes, final_nodes, labels):
            gr.add_edge(u, v, label=l)

        enfa = create_non_deterministic_automaton_from_graph(
            gr, start_nodes, final_nodes
        )

        for label in labels:
            assert enfa.accepts([label])

        path = [x for x in labels]
        assert enfa.accepts(path)

    def test_automata_from_graph_cfpq_data(self):
        graph_path = cfpq_data.download("skos")
        graph = cfpq_data.graph_from_csv(graph_path)
        enfa = create_non_deterministic_automaton_from_graph(graph)
        eps = Epsilon()
        for u, v, ddict in graph.edges(data=True):
            l = ddict.get("label", eps)
            assert enfa.accepts([l])
