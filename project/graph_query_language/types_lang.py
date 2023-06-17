from project.graph_query_language.exceptions import InvalidArgument
from pyformlang.finite_automaton import EpsilonNFA
from pyformlang import regular_expression as re
from typing import Union
import networkx as nx


# import sys
# sys.path.append('..')
from project.finite_automata import create_non_deterministic_automaton_from_graph
from project.intersection_finite_automata import get_intersection_two_finite_automata


def create_graph_from_enfa(enfa: EpsilonNFA) -> 'Graph':
    start_nodes = [x.value for x in enfa.start_states]
    final_nodes = [x.value for x in enfa.final_states]
    return Graph(graph=enfa.to_networkx(), start_nodes=start_nodes, final_nodes=final_nodes)


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
        raise InvalidArgument(f"no variable found with this name {self._value}")

    @property
    def value(self):
        return self._value

class String:
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return self.value
    
class Graph:
    def __init__(self, vertexes = None, edges = None, graph = None, start_nodes = None, final_nodes = None) -> None:
        self.gr = nx.MultiDiGraph()
        if graph is None and vertexes is not None and edges is not None:
            self.gr.add_nodes_from(vertexes)
            for edge in edges:
                self.gr.add_edge(edge.fst, edge.snd, label=edge.label.replace("\"", ''))
        else:
            self.gr = nx.MultiDiGraph(graph)
        if start_nodes is None:
            start_nodes = list(self.gr.nodes)
        self.start_nodes = start_nodes
        if final_nodes is None:
            final_nodes = list(self.gr.nodes)
        self.final_nodes = final_nodes
    
    def __str__(self) -> str:
        out = f'''Graph: 
    nodes: {self.get_vertices().__str__()}
    edges: {self.get_edges().__str__()}'''
        return out

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
        result = []
        for s, t  in nx.transitive_closure(nx.DiGraph(self.gr)).edges():
            if s in self.start_nodes and t in self.final_nodes:
                result.append((s, t));
        return result
    
    def get_vertices(self):
        return list(self.gr.nodes)

    def get_edges(self):
        result = []
        for u, v, l in self.gr.edges(data=True):
            for label in l.values():
                result.append((u, label, v)); 
        return result

    def get_labels(self):
        result = set()
        for _, _, l in self.gr.edges(data=True):
            for label in l.values():
                result.add(label); 
        return list(result)
    
    def intersect(self, entity: Union['Graph', 'Regex']) -> 'Graph':
        enfa_r = None
        if isinstance(entity, Graph):
            enfa_r = create_non_deterministic_automaton_from_graph(entity.gr, entity.start_nodes, entity.final_nodes)
        if isinstance(entity, Regex):
            enfa_r = entity.rgx.to_epsilon_nfa().minimize()
        if enfa_r is None:
            raise InvalidArgument(f"arguments of different types: {type(self)} != {type(entity)} or {type(entity)} != regex")
        enfa_l = create_non_deterministic_automaton_from_graph(self.gr, self.start_nodes, self.final_nodes)
        enfa = get_intersection_two_finite_automata(enfa_l, enfa_r)
        return create_graph_from_enfa(enfa)


    def concat(self, entity: Union['Graph', 'Regex']) -> 'Graph':
        regex_r = None
        if isinstance(entity, Graph):
            regex_r = create_non_deterministic_automaton_from_graph(entity.gr, entity.start_nodes, entity.final_nodes).minimize().to_regex()
        if isinstance(entity, Regex):
            regex_r = entity.rgx
        if regex_r is None:
            raise InvalidArgument(f"arguments of different types: {type(self)} != {type(entity)} or {type(entity)} != regex")
        regex_l = create_non_deterministic_automaton_from_graph(self.gr, self.start_nodes, self.final_nodes).minimize().to_regex()
        enfa = regex_l.concatenate(regex_r).to_epsilon_nfa().minimize()
        return create_graph_from_enfa(enfa)


    def union(self, entity: Union['Graph', 'Regex']) -> 'Graph':
        enfa_r = None
        if isinstance(entity, Graph):
            enfa_r = create_non_deterministic_automaton_from_graph(entity.gr, entity.start_nodes, entity.final_nodes).minimize()
        if isinstance(entity, Regex):
            enfa_r = entity.rgx.to_epsilon_nfa().minimize()
        if enfa_r is None:
            raise InvalidArgument(f"arguments of different types: {type(self)} != {type(entity)} or {type(entity)} != regex")
        enfa_l = create_non_deterministic_automaton_from_graph(self.gr, self.start_nodes, self.final_nodes).minimize()
        enfa = enfa_l.union(enfa_r).minimize()
        return create_graph_from_enfa(enfa)


    def inop(self, elem) -> 'Bool':
        res = elem in self.get_vertices() or elem in self.get_labels() or elem in self.get_edges()
        return Bool(res)


    def kleene(self) -> 'Graph':
        enfa_l = create_non_deterministic_automaton_from_graph(self.gr, self.start_nodes, self.final_nodes).minimize().to_regex()
        enfa = enfa_l.kleene_star().to_epsilon_nfa().minimize()
        return create_graph_from_enfa(enfa)


    def normilize(self):
        index = 0
        node_to_index = {}
        for node in self.gr.nodes:
            node_to_index[node] = index
            index += 1
        edges = []
        for u, l, v in self.get_edges():
            edges.append(Edge(node_to_index[u], l, node_to_index[v]))
        nodes = [node_to_index[x] for x in self.gr.nodes]
        start_nodes = [node_to_index[x] for x in self.start_nodes]
        final_nodes = [node_to_index[x] for x in self.final_nodes]
        return Graph(vertexes=nodes, edges=edges, start_nodes=start_nodes, final_nodes=final_nodes)


    def __eq__(self, graph: object) -> bool:
        return self.get_edges() == graph.get_edges()


class Regex:
    def __init__(self, regex_str: str ='', regex:'Regex' = None) -> None:
        if regex is None:
            regex_str = regex_str.replace('"','')
            regex = re.Regex(regex_str)
        self.rgx = regex


    def __str__(self) -> str:
        return self.rgx.__str__()


    def concat(self, regex: 'Regex') -> 'Regex':
        if type(self) != type(regex):
            raise InvalidArgument(f"arguments of different types: {type(self)} != {type(regex)}")
        return Regex(regex=self.rgx.concatenate(regex.rgx))


    def union(self, regex: 'Regex') -> 'Regex':
        if type(self) != type(regex):
            raise InvalidArgument(f"arguments of different types: {type(self)} != {type(regex)}")
        self.rgx.union(regex.rgx)
        return Regex(regex=self.rgx.union(regex.rgx))


    def kleene(self) -> 'Regex':
        return Regex(regex=self.rgx.kleene_star())


    def __eq__(self, regex: 'Regex') -> bool:
        return self.rgx == regex.rgx


class Bool:
    def __init__(self, value) -> None:
        self.value = value
    

    def __str__(self) -> str:
        return "true" if self.value else "false"


    def intersect(self, b: 'Bool') -> 'Bool':
        return Bool(self.value and b.value)


    def union(self, b: 'Bool') -> 'Bool':
        return Bool(self.value or b.value)


    def __eq__(self, b: 'Bool') -> bool:
        return self.value == b.value


class Lambda:
    def __init__(self, args, body) -> None:
        self.args = args
        self.body = body

    def __str__(self) -> str:
        lam = 'lambda: {'
        for x in self.args:
            lam += x.value + ', '
        if len(self.args) != 0:
            lam = lam[:-2]
        lam += '} -> body'
        return lam