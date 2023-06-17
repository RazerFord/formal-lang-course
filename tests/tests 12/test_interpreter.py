import sys


from project.graph_query_language.interpreter import interpreter


class TestInterpreter:
    def simple_test(self):
        sys.stdout = open('test_output', 'w')
        assert interpreter('print "hello world";')