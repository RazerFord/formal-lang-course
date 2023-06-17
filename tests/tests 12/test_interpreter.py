import sys


from project.graph_query_language.interpreter import interpreter
from pathlib import Path


FILENAME = 'test_output'


class Output:
    def acquire(self):
        self.out = open(FILENAME, 'w')
        self.out_print = sys.stdout
        sys.stdout = self.out

    def release(self) -> None:
        sys.stdout = self.out_print
        self.out.close()


def read_file(file: Path)-> str:
    text = file.open()
    return "".join(text.readlines())



class TestInterpreter:
    def test_hello_world(self):
        out = Output()
        out.acquire()
        interpreter('print "hello world";')
        out.release()
        ans = read_file(Path(FILENAME))
        assert "hello world" in ans

    def test_bind(self):
        out = Output()
        out.acquire()
        interpreter('''
        x := 19132;
        print x;
        x := 746;
        print x;''')
        out.release()
        ans = read_file(Path(FILENAME))
        assert "746" in ans
        assert "19132" in ans

        out.acquire()
        interpreter('''
        g := ({1, 2, 3, 4}, {(1, "a", 2), (3, "c", 4)});
        print g;
        ''')
        out.release()
        ans = read_file(Path(FILENAME))
        assert "Graph" in ans
        assert "nodes: [1, 2, 3, 4]" in ans
        assert "edges: [(1, 'a', 2), (3, 'c', 4)]" in ans

        out.acquire()
        interpreter('''
        g := ({}, {});
        print g;
        ''')
        out.release()
        ans = read_file(Path(FILENAME))
        assert "Graph" in ans
        assert "nodes: []" in ans
        assert "edges: []" in ans


    def test_map_fst_snd(self):
        out = Output()
        out.acquire()
        interpreter('''
        fst := (lambda {x, y} -> x);
        snd := (lambda {x, y} -> y);
        list := {{1, 2}, {2, 3}, {3, 2}, {2, 1}};
        print map fst : list;
        print map snd : list;
        ''')
        out.release()
        ans = read_file(Path(FILENAME))
        assert "[1, 2, 3, 2]" in ans
        assert "[2, 3, 2, 1]" in ans

    def test_map_get(self):
        out = Output()
        out.acquire()
        prog = self.prog_getter('get_start')
        interpreter(prog)
        out.release()
        ans = read_file(Path(FILENAME))
        assert "[1, 2, 3, 4]" in ans
        assert "[5, 7, 9, 10]" in ans
        out.acquire()
        prog = self.prog_getter('get_final')
        interpreter(prog)
        out.release()
        ans = read_file(Path(FILENAME))
        assert "[1, 2, 3, 4]" in ans
        assert "[5, 7, 9, 10]" in ans


    def test_map_set(self):
        out = Output()
        out.acquire()
        prog = self.prog_setter('get_start', 'set_start', '46, 47, 49')
        interpreter(prog)
        out.release()
        ans = read_file(Path(FILENAME))
        assert "[46, 47, 49]" in ans
        out.acquire()
        prog = self.prog_setter('get_final', 'set_final', '46, 47, 49')
        interpreter(prog)
        out.release()
        ans = read_file(Path(FILENAME))
        assert "[46, 47, 49]" in ans


    def test_map_add(self):
        out = Output()
        out.acquire()
        prog = self.prog_setter('get_start', 'add_start', '46, 47, 49')
        interpreter(prog)
        out.release()
        ans = read_file(Path(FILENAME))
        assert "[1, 2, 3, 4, 46, 47, 49]" in ans
        assert "[5, 7, 9, 10, 46, 47, 49]" in ans
        out.acquire()
        prog = self.prog_setter('get_final', 'add_final', '46, 47, 49')
        interpreter(prog)
        out.release()
        ans = read_file(Path(FILENAME))
        assert "[1, 2, 3, 4, 46, 47, 49]" in ans
        assert "[5, 7, 9, 10, 46, 47, 49]" in ans


    # def test_bind_fail(self):
    #     out = Output()
    #     out.acquire()
    #     interpreter('''
    #     x := 19132;
    #     x := true;
    #     print x;''', True)
    #     out.release()
    #     ans = read_file(Path(FILENAME))
    #     assert "assigning a declared variable an argument of a different type" in ans

    def prog_getter(self, cmd:str) -> str:
        return '''strt := (lambda {z} -> '''+cmd+''' of z);
        g1 := ({1, 2, 3, 4}, {(1, "a", 2), (3, "c", 4)});
        g2 := ({5, 7, 9, 10}, {(5, "a", 7), (9, "c", 10)});
        list := {g1, g2};
        print map strt : list;
        '''
    
    def prog_setter(self, get:str,cmd:str, vertexes: str) -> str:
        return '''get := (lambda {z} -> '''+get+''' of z);
        set := (lambda {z} -> '''+cmd+''' of {'''+vertexes+'''} to z);
        g1 := ({1, 2, 3, 4}, {(1, "a", 2), (3, "c", 4)});
        g2 := ({5, 7, 9, 10}, {(5, "a", 7), (9, "c", 10)});
        list := {g1, g2};
        list := map set : list;
        print map get : list;
        '''