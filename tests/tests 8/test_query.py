import data
from project.cfpq import cfpq_hellings
from pyformlang.cfg import Variable


class TestQuery:
    def test_simple_unreachable(self):
        result = cfpq_hellings(data.graph_simple(), data.cfg_simple(), None, {2}, {1})
        assert len(result) == 0

    def test_simple_reachable(self):
        result = cfpq_hellings(data.graph_simple(), data.cfg_simple(), None, {1}, {2})
        u, v = result.pop()
        assert u == 1 and v == 2

    def test_hard_reacheable(self):
        result = cfpq_hellings(
            data.graph_hard(), data.cfg_hard(), Variable("S1"), {0}, {3, 2, 1}
        )
        assert len(result) == 2

    def test_hard_reacheable(self):
        result = cfpq_hellings(data.graph_hard(), data.cfg_hard(), Variable("A"))
        assert len(result) == 3
