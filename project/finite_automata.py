from pyformlang.finite_automaton import (
    EpsilonNFA,
    Epsilon,
    DeterministicFiniteAutomaton,
)
from pyformlang.regular_expression import Regex
from networkx import MultiDiGraph


def create_deterministic_automaton_from_regex(
    regex_expr: str,
) -> DeterministicFiniteAutomaton:
    """
    Parameters
    ----------
    regex_expr : str
        Regular expression written as a string

    Returns
    ----------
    DeterministicFiniteAutomaton
        Return minimum DFA
    """
    return Regex(regex_expr).to_epsilon_nfa().minimize()


def create_non_deterministic_automaton_from_graph(
    graph: MultiDiGraph, start_nodes: list = None, final_nodes: list = None
) -> EpsilonNFA:
    """
    Parameters
    ----------
    graph : MultiDiGraph
        The graph from which nfa is built
    start_nodes : list
        List of starting nodes
    final_nodes : list
        List of final nodes

    Returns
    ----------
    EpsilonNFA
        Return NFA
    """
    enfa = EpsilonNFA()
    states = graph.nodes

    if start_nodes is None:
        start_nodes = states
    if final_nodes is None:
        final_nodes = states

    for v in start_nodes:
        enfa.add_start_state(v)
    for v in final_nodes:
        enfa.add_final_state(v)

    eps = Epsilon()
    for u, v, ddict in graph.edges(data=True):
        symbol = ddict.get("label", eps)
        enfa.add_transition(u, symbol, v)

    return enfa
