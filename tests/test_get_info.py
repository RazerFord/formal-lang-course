from graphs import graphs
from project.graph_info import get_info


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

    def helper_check_graph(self, name):
        num_node, num_edge, true_labels = graphs[name].values()
        num_node_s, num_edge_s, labels = get_info(name)
        is_equal = (
            num_node == num_node_s and num_edge == num_edge_s and true_labels == labels
        )
        return is_equal
