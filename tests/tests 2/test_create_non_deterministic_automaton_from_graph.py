from graph import graph
from networkx import MultiDiGraph, single_source_shortest_path
from project.finite_automata import create_non_deterministic_automaton_from_graph
from pyformlang.finite_automaton import Epsilon
from numpy import argmax
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

        for _, _, ddict in graph.edges(data=True):
            l = ddict.get("label", eps)
            assert enfa.accepts([l])

    def test_label_on_path_automata_from_graph_cfpq_data(self):
        graph_path = cfpq_data.download("skos")
        graph = cfpq_data.graph_from_csv(graph_path)
        list_paths = single_source_shortest_path(graph, 0)
        arg_max_len = argmax([len(p) for _, p in list_paths.items()])
        path = list(list_paths.items())[arg_max_len][1]
        eps = Epsilon()
        labels = []

        for u, v in zip(path, path[1:]):
            label = graph.get_edge_data(u, v, key=0).get("label", eps)
            labels.append(label)

        enfa = create_non_deterministic_automaton_from_graph(graph)
        assert enfa.accepts(labels)
