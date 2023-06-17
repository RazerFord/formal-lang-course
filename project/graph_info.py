import cfpq_data
import networkx
from collections import namedtuple

GraphInfo = namedtuple("GraphInfo", "number_of_nodes number_of_edges labels")


def get_graph_info_by_name(graph_name: str) -> GraphInfo:
    graph = get_graph_by_name(graph_name)

    labels = parse_labels(graph)
    graph_info = GraphInfo(graph.number_of_nodes(), graph.number_of_edges(), labels)

    return graph_info


def get_graph_by_name(graph_name: str) -> networkx.MultiDiGraph:
    graph_path = cfpq_data.download(graph_name)
    return cfpq_data.graph_from_csv(graph_path)


def parse_labels(graph) -> set:
    labels = set()
    for _, _, ddict in graph.edges(data=True):
        label = ddict.get("label", None)
        if label is not None:
            labels.add(label)
    return labels


def create_and_save_graph_two_cycles(
    num_node_fst: int, num_node_snd: int, labels: set, path: str = "out.dot"
) -> None:
    graph = cfpq_data.labeled_two_cycles_graph(
        num_node_fst, num_node_snd, labels=labels
    )
    graph = networkx.drawing.nx_pydot.to_pydot(graph)
    graph.write_raw(path)
