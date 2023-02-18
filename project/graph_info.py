import cfpq_data
import networkx


def get_info(graph_name: str):
    graph_path = cfpq_data.download(graph_name)
    graph = cfpq_data.graph_from_csv(graph_path)
    count_nodes, count_edges = graph.number_of_nodes(), graph.number_of_edges()
    labels = set()
    for v, u in graph.edges():
        if "label" in graph.get_edge_data(v, u, 0, {}):
            labels.add(graph.get_edge_data(v, u, 0, {})["label"])

    return count_nodes, count_edges, labels


def create_graph_two_cycles(
    count_node_first, count_node_second, labels, file_name="output.dot"
):
    graph = cfpq_data.labeled_two_cycles_graph(
        count_node_first, count_node_second, labels=labels
    )
    graph = networkx.drawing.nx_pydot.to_pydot(graph)
    graph.write_raw(file_name)
