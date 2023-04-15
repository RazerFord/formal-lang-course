
from project.hellings_reachability import hellings
import data

class TestHellings:
    def test_simple_helings(self):
        result = hellings(data.graph_simple(), data.cfg_simple())
        assert result == data.answer_simple()

    def test_hard_helings(self):
        result = hellings(data.graph_hard(), data.cfg_hard())
        assert result == data.answer_hard()
