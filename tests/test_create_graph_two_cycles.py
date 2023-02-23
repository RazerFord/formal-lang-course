from project.graph_info import create_graph_two_cycles
import pydot
import cfpq_data
import pathlib


class TestCreateGraphTwoCycles:
    def test_one(self):
        num_node_first = 3
        num_node_second = 2
        labels = ("a", "b")
        create_graph_two_cycles(num_node_first, num_node_second, labels)
        self.helper_comparison_graph(num_node_first, num_node_second, labels)

    def test_two(self):
        num_node_first = 6
        num_node_second = 4
        labels = ("x", "z")
        create_graph_two_cycles(num_node_first, num_node_second, labels)
        self.helper_comparison_graph(num_node_first, num_node_second, labels)

    def test_three(self):
        num_node_first = 49
        num_node_second = 42
        labels = ("a", "z")
        create_graph_two_cycles(num_node_first, num_node_second, labels)
        self.helper_comparison_graph(num_node_first, num_node_second, labels)

    def test_four(self):
        num_node_first = 30
        num_node_second = 30
        labels = ("x", "z")
        create_graph_two_cycles(num_node_first, num_node_second, labels)
        self.helper_comparison_graph(num_node_first, num_node_second, labels)

    def test_five(self):
        num_node_first = 300
        num_node_second = 99
        labels = ("g", "z")
        create_graph_two_cycles(num_node_first, num_node_second, labels)
        self.helper_comparison_graph(num_node_first, num_node_second, labels)

    def helper_comparison_graph(
        self, num_node_first, num_nodes_secod, labels, file_name="output.dot"
    ):
        graph_file = pydot.graph_from_dot_file(file_name)[0]
        graph = cfpq_data.labeled_two_cycles_graph(
            num_node_first, num_nodes_secod, labels=labels
        )

        num_node_file = len(graph_file.get_nodes()) - 1
        num_node_graph = graph.number_of_nodes()

        if num_node_file != num_node_graph:
            return True

        for first, second in zip(graph.edges(), graph_file.get_edges()):
            first_from, first_to = first
            first_label = graph.get_edge_data(first_from, first_to, 0, {})["label"]
            first_graph = (first_from, first_to, first_label)

            second_from = second.get_source()
            second_to = second.get_destination()
            second_label = second.get_label()
            second_graph = (second_from, second_to, second_label)

            is_equal = first_graph == second_graph
            if not is_equal:
                return False

    def __del__(self):
        path = str(pathlib.Path(__file__).parent.parent) + "/output.dot"
        link = pathlib.Path(path)
        if link.is_file():
            link.unlink()
