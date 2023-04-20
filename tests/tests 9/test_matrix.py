import data
from project.matrix import matrix


class TestMatrix:
    def test_hard(self):
        cfga = data.cfg_hard()
        graph = data.graph_hard()
        assert data.answer_hard() == matrix(graph, cfga)
