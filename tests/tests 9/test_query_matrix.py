import data_test_9 as data
from project.cfpq import cfpq_matrix
from pyformlang.cfg import Variable


class TestQueryMatrix:
    def test_simple_unreachable(self):
        result = cfpq_matrix(data.graph_simple(), data.cfg_simple(), None, {2}, {1})
        assert len(result) == 0

    def test_simple_reachable(self):
        result = cfpq_matrix(data.graph_simple(), data.cfg_simple(), None, {1}, {2})
        u, v = result.pop()
        assert u == 1 and v == 2

    def test_hard_first_reacheable(self):
        result = cfpq_matrix(
            data.graph_hard(), data.cfg_first_hard(), Variable("S1"), {0}, {3, 2, 1}
        )
        assert len(result) == 1
        result = cfpq_matrix(data.graph_hard(), data.cfg_first_hard(), Variable("A"))
        assert len(result) == 3

    def test_hard_second_reacheable(self):
        result = cfpq_matrix(
            data.graph_hard(), data.cfg_second_hard(), Variable("B"), {0}, {3, 2, 1}
        )
        assert len(result) == 1
