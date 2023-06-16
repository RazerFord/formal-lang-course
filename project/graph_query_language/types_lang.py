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
        self.gr = nx.MultiGraph()
        self.gr.add_nodes_from(vertexes)
        for edge in edges:
            self.gr.add_edge(edge.fst, edge.snd, label=edge.label)
    
    def __str__(self) -> str:
        return self.gr.__str__()
