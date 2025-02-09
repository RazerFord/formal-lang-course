from project.hellings import hellings
import data_test_8 as data


class TestHellings:
    def test_simple_helings(self):
        result = hellings(data.graph_simple(), data.cfg_simple())
        assert result == data.answer_simple()

    def test_hard_helings(self):
        result = hellings(data.graph_hard(), data.cfg_hard())
        assert result == data.answer_hard()
