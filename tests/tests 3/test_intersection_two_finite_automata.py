import networkx as nx
from project.intersection_finite_automata import get_intersection_two_finite_automata
from project.finite_automata import create_non_deterministic_automaton_from_graph
from project.finite_automata import create_deterministic_automaton_from_regex


class TestIntersectionTwoFiniteAutomata:
    def test_intersect_from_graph(self):
        fst_dfa = self.create_dfa_fst()
        snd_dfa = self.create_dfa_snd()

        my_intersection = get_intersection_two_finite_automata(fst_dfa, snd_dfa)
        intersection = fst_dfa.get_intersection(snd_dfa)
        assert my_intersection == intersection

        my_intersection = get_intersection_two_finite_automata(snd_dfa, fst_dfa)
        intersection = snd_dfa.get_intersection(fst_dfa)
        assert my_intersection == intersection

    def test_intersect_from_regex(self):
        fst_regex_expr = "xyz|owq"
        snd_regex_expr = "abc|xyz|psq"
        fst_dfa = create_deterministic_automaton_from_regex(fst_regex_expr)
        snd_dfa = create_deterministic_automaton_from_regex(snd_regex_expr)

        my_intersection = get_intersection_two_finite_automata(fst_dfa, snd_dfa)
        intersection = fst_dfa.get_intersection(snd_dfa)
        assert my_intersection == intersection

        my_intersection = get_intersection_two_finite_automata(snd_dfa, fst_dfa)
        intersection = snd_dfa.get_intersection(fst_dfa)
        assert my_intersection == intersection

    def create_dfa_fst(self):
        gr = nx.MultiDiGraph()
        start_nodes = [0, 1]
        final_nodes = [1, 0]
        labels = ["a", "b"]

        for u, v, l in zip(start_nodes, final_nodes, labels):
            gr.add_edge(u, v, label=l)
        enfa = create_non_deterministic_automaton_from_graph(
            gr, start_nodes, final_nodes
        )
        return enfa

    def create_dfa_snd(self):
        gr = nx.MultiDiGraph()
        start_nodes = [0, 0]
        final_nodes = [0, 0]
        labels = ["a", "b"]

        for u, v, l in zip(start_nodes, final_nodes, labels):
            gr.add_edge(u, v, label=l)
        enfa = create_non_deterministic_automaton_from_graph(
            gr, list(set(start_nodes)), list(set(final_nodes))
        )
        return enfa
