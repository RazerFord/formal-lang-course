import data_test_9 as data
from project.matrix import matrix


class TestMatrix:
    def test_simple(self):
        cfg = data.cfg_simple()
        graph = data.graph_simple()
        assert matrix(graph, cfg) == data.answer_simple()

    def test_hard_first(self):
        cfg = data.cfg_first_hard()
        graph = data.graph_hard()
        assert matrix(graph, cfg) == data.answer_hard_first()

    def test_hard_second(self):
        cfg = data.cfg_second_hard()
        graph = data.graph_hard()
        assert matrix(graph, cfg) == data.answer_hard_second()
