from exceptions import InvalidArgument
import networkx as nx

class Edge:
    def __init__(self, fst, label, snd) -> None:
        self.fst = fst
        self.label = label
        self.snd = snd

    def __str__(self) -> str:
        return "Edge: ({0}, {1}, {2})".format(self.fst, self.label, self.snd)

class Id:
    def __init__(self, value, memory) -> None:
        self._value = value
        self.memory = memory

    def __str__(self) -> str:
        if self.memory.contains(self):
            return str(self.memory[self])
        raise InvalidArgument("no variable found with this name")

    @property
    def value(self):
        return self._value

class String:
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return self.value
    
class Graph:
    def __init__(self, vertexes, edges) -> None:
        self.gr = nx.MultiDiGraph()
        self.gr.add_nodes_from(vertexes)
        for edge in edges:
            self.gr.add_edge(edge.fst, edge.snd, label=edge.label)
        self.start_nodes = list(self.gr.nodes)
        self.final_nodes = list(self.gr.nodes)
    
    def __str__(self) -> str:
        return self.gr.__str__()

    def set_start_nodes(self, nodes:list[int]):
        self.gr.add_nodes_from(nodes)
        self.start_nodes = nodes
    
    def set_final_nodes(self, nodes:list[int]):
        self.gr.add_nodes_from(nodes)
        self.final_nodes = nodes

    def add_start_nodes(self, nodes:list[int]):
        self.gr.add_nodes_from(nodes)
        self.start_nodes += nodes
    
    def add_final_nodes(self, nodes:list[int]):
        self.gr.add_nodes_from(nodes)
        self.final_nodes += nodes

    def get_reachable(self):
        return list(nx.transitive_closure(nx.DiGraph(self.gr)).edges())

class Bool:
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return "true" if self.value else "false"
