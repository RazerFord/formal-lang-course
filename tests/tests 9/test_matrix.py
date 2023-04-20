import data_test_9 as data
from project.matrix import matrix


class TestMatrix:
    def test_hard_first(self):
        cfga = data.cfg_first_hard()
        graph = data.graph_hard()
        assert data.answer_hard_first() == matrix(graph, cfga)

    def test_hard_second(self):
        cfga = data.cfg_second_hard()
        graph = data.graph_hard()
        assert data.answer_hard_second() == matrix(graph, cfga)
