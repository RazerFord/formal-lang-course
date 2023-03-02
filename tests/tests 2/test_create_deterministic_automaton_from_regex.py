from pyformlang.regular_expression import Regex
from project.finite_automata import create_deterministic_automaton_from_regex
from expressions import tests


class TestCreateDeterministicAutomatonFromRegex:
    def test_one(self):
        regex_expr = "|".join(tests[0]["expressions"])
        automaton = create_deterministic_automaton_from_regex(regex_expr)
        regex = Regex(regex_expr)

        for word in tests[0]["regex_true"]:
            assert regex.accepts(word) == automaton.accepts(word) and regex.accepts(
                word
            )

        for word in tests[0]["regex_false"]:
            assert regex.accepts(word) == automaton.accepts(word) and not regex.accepts(
                word
            )

    def test_two(self):
        regex_expr = "|".join(tests[1]["expressions"])
        automaton = create_deterministic_automaton_from_regex(regex_expr)
        regex = Regex(regex_expr)

        for word in tests[1]["regex_true"]:
            assert regex.accepts(word) == automaton.accepts(word) and regex.accepts(
                word
            )

        for word in tests[1]["regex_false"]:
            assert regex.accepts(word) == automaton.accepts(word) and not regex.accepts(
                word
            )

    def test_three(self):
        regex_expr = ".".join(tests[2]["expressions"])
        automaton = create_deterministic_automaton_from_regex(regex_expr)
        regex = Regex(regex_expr)

        for word in tests[2]["regex_true"]:
            assert regex.accepts(word) == automaton.accepts(word) and regex.accepts(
                word
            )

        for word in tests[2]["regex_false"]:
            assert regex.accepts(word) == automaton.accepts(word) and not regex.accepts(
                word
            )
