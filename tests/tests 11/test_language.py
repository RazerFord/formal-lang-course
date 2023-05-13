from project.graph_query_language.parser import check_input
from project.graph_query_language.parser import TreeListener
import expected_graph as eg
import os


class TestLanguage:
    def test_comment(self):
        assert check_input("x := 1; //this random text")
        assert check_input(
            """
        //this random text
        x := 1;
        """
        )
        assert check_input(
            """
        x := 1;
        //this random text
        """
        )

    def test_var(self):
        assert check_input('z :="text";')
        assert check_input("z := 1234567890;")
        assert check_input("_z1 :=124124;")

        assert check_input('e :=(1, "a", 1123);')
        assert check_input('e :={41, "b", 23};')
        assert check_input('list :={true, false, "str"};')

        assert check_input('g :=({(1, "a", 2), (2, "b", 3), (3, "c", 1)}, {1, 2, 3});')

    def test_func(self):
        assert check_input("graph := (set_start of list to graph);")
        assert check_input("graph := (add_start of list to graph);")
        assert check_input("graph := (set_final of list to graph);")
        assert check_input("graph := (add_final of list to graph);")

        assert check_input("list := (get_final of graph);")
        assert check_input("list := (get_start of graph);")
        assert check_input("list := (get_reachable of graph);")
        assert check_input("list := (get_vertices of graph);")
        assert check_input("list := (get_edges of graph);")
        assert check_input("list := (get_labels of graph);")

    def test_functional(self):
        assert check_input("fn :=(lambda {x, y} -> x & y | x);")
        assert check_input("f := (map (lambda {x, y} -> xy) per);")
        assert check_input("f := (filter (lambda {x, y} -> xy) per);")

    def test_load(self):
        assert check_input("gr := (load path);")
        assert check_input('gr := (load "sorce");')

    def test_operator(self):
        assert check_input("g := g1 & g2;")
        assert check_input("g := g1 . g2;")
        assert check_input("g := g1 | g2;")
        assert check_input("g := g1 in g2;")
        assert check_input("g := g1*;")

    def test_fail(self):
        assert not check_input("load (map (lambda {x, y} -> xy) per);")
        assert not check_input("g := g1 & g := g2;")
        assert not check_input("g := g1 in := 2;")

    def test_commbine(self):
        assert check_input('g := (map (lambda {x, y} -> xy) load "graph");')
        assert check_input('g := (filter (lambda {x, y} -> true) load "graph");')
        assert check_input(
            'g := (map (lambda {x, y} -> x) load "graph") & (filter (lambda {x, y} -> false) load "graph");'
        )

    def test_tree(self):
        path = "path.dot"
        TreeListener("s := 1;").save_in_dot(path)
        f = open(path, mode="r")
        text = f.read()
        print(text)
        f.close()
        assert eg.tree == text
        if os.path.exists(path):
            os.remove(path)
