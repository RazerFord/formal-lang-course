from project.graph_query_language.parser import check_input


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
        assert check_input("f := (map (lambda {x, y} -> xy) asd);")
        assert check_input("f := (filter (lambda {x, y} -> xy) asd);")

    def test_load(self):
        assert check_input("gr := (load path);")
        assert check_input('gr := (load "sorce");')

    def test_operator(self):

        assert check_input("g := g1 & g2;")
        assert check_input("g := g1 . g2;")
        assert check_input("g := g1 | g2;")
        assert check_input("g := g1 in g2;")
        assert check_input("g := g1*;")
