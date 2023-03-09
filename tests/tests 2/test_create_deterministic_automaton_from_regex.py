from pyformlang.regular_expression import Regex
from pyformlang.finite_automaton import EpsilonNFA
from project.finite_automata import create_deterministic_automaton_from_regex
from expressions import tests


class TestCreateDeterministicAutomatonFromRegex:
    def test_without_regex(self):
        regex_expr = "a|bc|d"
        enfa = EpsilonNFA()
        enfa.add_start_state(0)
        enfa.add_final_state(1)
        enfa.add_transition(0, "a", 1)
        enfa.add_transition(0, "bc", 1)
        enfa.add_transition(0, "d", 1)

        enfa_created = create_deterministic_automaton_from_regex(regex_expr)

        assert enfa.accepts(["a"]) == enfa_created.accepts(["a"])
        assert enfa.accepts(["bc"]) == enfa_created.accepts(["bc"])
        assert enfa.accepts(["d"]) == enfa_created.accepts(["d"])

    def test_union(self):
        regex_expr = "|".join(tests[0]["expressions"])
        self.helper(regex_expr, 0)

    def test_concatenation(self):
        regex_expr = ".".join(tests[1]["expressions"])
        self.helper(regex_expr, 1)

    def test_union_and_concatenation(self):
        regex_expr = "|".join(tests[2]["expressions"])
        self.helper(regex_expr, 2)

    def helper(self, regex_expr: str, number: int):
        automaton = create_deterministic_automaton_from_regex(regex_expr)
        regex = Regex(regex_expr)

        for word in tests[number]["regex_true"]:
            r_word = regex.accepts(word)
            a_word = automaton.accepts(word)

            assert r_word == a_word and r_word

        for word in tests[number]["regex_false"]:
            r_word = regex.accepts(word)
            a_word = automaton.accepts(word)

            assert r_word == a_word and not r_word
