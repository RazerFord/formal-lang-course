import pytest
from project.graph_info import get_info
from graphs import graphs


class TestGetInfo:
    def test_graph_skos(self):
        assert self.helper_check_graph("skos")

    def test_graph_generations(self):
        assert self.helper_check_graph("generations")

    def test_graph_foaf(self):
        assert self.helper_check_graph("foaf")

    def test_graph_pr(self):
        assert self.helper_check_graph("pr")

    def test_graph_gzip(self):
        assert self.helper_check_graph("gzip")

    def helper_check_graph(self, graph):
        num_node, num_edge, true_labels = graphs[graph].values()
        count_node, count_edge, labels = get_info(graph)
        return (
            num_node == count_node and num_edge == count_edge and true_labels == labels
        )
