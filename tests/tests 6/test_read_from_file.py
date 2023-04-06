from project.context_free_grammar import read_cfg_from_file
from project.context_free_grammar import read_wcfg_from_file
from pyformlang import cfg
from test_cfg_to_wcnf import equals
import pathlib


class TestReadFromFile:
    FILES = []
    ANSWER = []

    def test_first(self):
        self.init_first_test()
        name = self.FILES[0]
        ans = self.ANSWER[0]
        cfg_gr = read_cfg_from_file(name)
        assert equals(ans, cfg_gr)

    def test_second(self):
        self.init_second_test()
        name = self.FILES[1]
        ans = self.ANSWER[1]
        cfg_gr = read_cfg_from_file(name)
        assert equals(ans, cfg_gr)

    def test_third(self):
        self.init_third_test()
        name = self.FILES[2]
        ans = self.ANSWER[2]
        cfg_gr = read_cfg_from_file(name)
        print("<" * 100)
        print(cfg_gr.to_text())
        print()
        print(ans.to_text())
        print("<" * 100)
        assert equals(ans, cfg_gr)

    def init_first_test(self):
        cfg_txt = """
        S -> A S A | a B
        A -> B | S
        B -> b | $
        """
        self.ANSWER.append(self.init_first_graph())
        self.create_test_file("first_text_file.txt", cfg_txt)

    def init_first_graph(self) -> cfg.CFG:
        S = cfg.Variable("S")
        A = cfg.Variable("A")
        B = cfg.Variable("B")
        a = cfg.Terminal("a")
        b = cfg.Terminal("b")
        prods = []
        prods.append(cfg.Production(S, [A, S, A]))
        prods.append(cfg.Production(S, [a, B]))
        prods.append(cfg.Production(A, [B]))
        prods.append(cfg.Production(A, [S]))
        prods.append(cfg.Production(B, [b]))
        prods.append(cfg.Production(B, [cfg.Epsilon()]))
        return cfg.CFG(
            {S, A, B},
            {a, b},
            S,
            set(prods),
        )

    def init_second_test(self):
        cfg_txt = """
        S -> A
        A -> B C
        B -> C
        C -> a
        """
        self.ANSWER.append(self.init_second_graph())
        self.create_test_file("second_text_file.txt", cfg_txt)

    def init_second_graph(self) -> cfg.CFG:
        S = cfg.Variable("S")
        A = cfg.Variable("A")
        B = cfg.Variable("B")
        C = cfg.Variable("C")
        a = cfg.Terminal("a")
        prods = []
        prods.append(cfg.Production(S, [A]))
        prods.append(cfg.Production(A, [B, C]))
        prods.append(cfg.Production(B, [C]))
        prods.append(cfg.Production(C, [a]))
        return cfg.CFG({S, A, B, C}, {a}, S, set(prods))

    def init_third_test(self):
        cfg_txt = """
        S -> A G
        A -> B C
        D -> $
        G -> K
        B -> C
        C -> a
        """
        self.ANSWER.append(self.init_third_graph())
        self.create_test_file("third_text_file.txt", cfg_txt)

    def init_third_graph(self) -> cfg.CFG:
        S = cfg.Variable("S")
        G = cfg.Variable("G")
        A = cfg.Variable("A")
        B = cfg.Variable("B")
        D = cfg.Variable("D")
        K = cfg.Variable("K")
        C = cfg.Variable("C")
        a = cfg.Terminal("a")
        prods = []
        prods.append(cfg.Production(S, [A, G]))
        prods.append(cfg.Production(A, [B, C]))
        prods.append(cfg.Production(D, [cfg.Epsilon()]))
        prods.append(cfg.Production(G, [K]))
        prods.append(cfg.Production(B, [C]))
        prods.append(cfg.Production(C, [a]))
        return cfg.CFG({S, A, B, C, G, D, K}, {a}, S, set(prods))

    def create_test_file(self, name: str, cfg_txt: str):
        self.FILES.append(name)
        with open(name, "w") as cin:
            cin.write(cfg_txt)

    def __del__(self):
        for name in self.FILES:
            path = str(pathlib.Path(__file__).parent.parent.parent) + f"/{name}"
            link = pathlib.Path(path)
            if link.is_file():
                link.unlink()
