from project.graph_info import create_graph_two_cycles
import pydot
import cfpq_data
import pathlib


class TestCreateGraphTwoCycles:
    def test_one(self):
        count_nodes_first = 3
        count_nodes_second = 2
        labels = ("a", "b")
        create_graph_two_cycles(count_nodes_first, count_nodes_second, labels)
        self.helper_comparison_graph(count_nodes_first, count_nodes_second, labels)

    def test_two(self):
        count_nodes_first = 6
        count_nodes_second = 4
        labels = ("x", "z")
        create_graph_two_cycles(count_nodes_first, count_nodes_second, labels)
        self.helper_comparison_graph(count_nodes_first, count_nodes_second, labels)

    def test_three(self):
        count_nodes_first = 49
        count_nodes_second = 42
        labels = ("a", "z")
        create_graph_two_cycles(count_nodes_first, count_nodes_second, labels)
        self.helper_comparison_graph(count_nodes_first, count_nodes_second, labels)

    def helper_comparison_graph(
        self, count_nodes_first, count_nodes_secod, labels, file_name="output.dot"
    ):
        graph_file = pydot.graph_from_dot_file(file_name)[0]
        graph = cfpq_data.labeled_two_cycles_graph(
            count_nodes_first, count_nodes_secod, labels=labels
        )

        count_nodes_file = len(graph_file.get_nodes()) - 1
        count_nodes_graph = graph.number_of_nodes()

        if count_nodes_file != count_nodes_graph:
            return True

        for first, second in zip(graph.edges(), graph_file.get_edges()):
            v_first, u_first = first
            label_first = graph.get_edge_data(v_first, u_first, 0, {})["label"]
            v_second, u_second = second.get_source(), second.get_destination()
            label_second = second.get_label()
            if (
                v_first != v_second
                and u_first != u_second
                and label_first != label_second
            ):
                return False

    def __del__(self):
        path = str(pathlib.Path(__file__).parent.parent) + "/output.dot"
        link = pathlib.Path(path)
        if link.is_file():
            link.unlink()
