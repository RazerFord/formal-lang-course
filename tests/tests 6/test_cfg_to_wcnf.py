from project.context_free_grammar import cfg_to_wcnf
from pyformlang import cfg


def equals(fst_cfg: cfg.CFG, snd_cfg: cfg.CFG) -> bool:
    return (
        fst_cfg.variables == snd_cfg.variables
        and fst_cfg.start_symbol == snd_cfg.start_symbol
        and fst_cfg.productions == snd_cfg.productions
    )


class TestCfgToWcnf:
    def test_first(self):
        test_cfg, answer_wcnf = self.init_first_test()
        wcnf = cfg_to_wcnf(test_cfg)
        assert equals(answer_wcnf, wcnf)

    def test_second(self):
        test_cfg, answer_wcnf = self.init_second_test()
        wcnf = cfg_to_wcnf(test_cfg)
        assert equals(answer_wcnf, wcnf)

    def test_third(self):
        test_cfg, answer_wcnf = self.init_third_test()
        wcnf = cfg_to_wcnf(test_cfg)
        assert equals(answer_wcnf, wcnf)

    def init_first_test(self) -> tuple[cfg.CFG, cfg.CFG]:
        S = cfg.Variable("S")
        A = cfg.Variable("A")
        B = cfg.Variable("B")
        E = cfg.Variable("E")
        F = cfg.Variable("F")
        a = cfg.Terminal("a")
        f = cfg.Terminal("f")
        s = cfg.Terminal("s")
        prods = []
        prods.append(cfg.Production(S, [A, S]))
        prods.append(cfg.Production(S, [B, S]))
        prods.append(cfg.Production(S, [s]))
        prods.append(cfg.Production(E, [E, F]))
        prods.append(cfg.Production(E, [F, F]))
        prods.append(cfg.Production(A, [a]))
        prods.append(cfg.Production(F, [f]))
        test_cfg = cfg.CFG(
            {S, A, B, E, F},
            {a, f, s},
            S,
            set(prods),
        )
        answer_prods = []
        answer_prods.append(cfg.Production(S, [s]))
        answer_prods.append(cfg.Production(S, [A, S]))
        answer_prods.append(cfg.Production(A, [a]))
        answer_wcnf = cfg.CFG({S, A}, {s, a}, S, set(answer_prods))
        return test_cfg, answer_wcnf

    def init_second_test(self) -> tuple[cfg.CFG, cfg.CFG]:
        S = cfg.Variable("S")
        A = cfg.Variable("A")
        B = cfg.Variable("B")
        C = cfg.Variable("C")
        a = cfg.Terminal("a")
        prod0 = cfg.Production(A, [C])
        prod1 = cfg.Production(S, [A])
        prod2 = cfg.Production(B, [cfg.Epsilon()])
        prod3 = cfg.Production(C, [a])
        prod4 = cfg.Production(A, [S])
        test_cfg = cfg.CFG({S, A, B, C}, {a}, S, {prod0, prod1, prod2, prod3, prod4})

        answer_prods = []
        answer_prods.append(cfg.Production(S, [a]))
        answer_wcnf = cfg.CFG({S}, {a}, S, set(answer_prods))
        return test_cfg, answer_wcnf

    def init_third_test(self) -> cfg.CFG:
        S = cfg.Variable("S")
        B = cfg.Variable("B")
        C = cfg.Variable("C")
        D = cfg.Variable("D")
        a = cfg.Terminal("a")
        b = cfg.Terminal("b")
        c = cfg.Terminal("c")
        prod0 = cfg.Production(S, [B])
        prod1 = cfg.Production(S, [a])
        prod2 = cfg.Production(B, [C])
        prod3 = cfg.Production(B, [b])
        prod4 = cfg.Production(C, [D, D])
        prod5 = cfg.Production(C, [c])
        prod6 = cfg.Production(D, [cfg.Epsilon()])
        test_cfg = cfg.CFG(
            {S, B, C, D},
            {a, b, c},
            S,
            {prod0, prod1, prod2, prod3, prod4, prod5, prod6},
        )

        answer_prods = []
        answer_prods.append(cfg.Production(S, [a]))
        answer_prods.append(cfg.Production(S, [b]))
        answer_prods.append(cfg.Production(S, [c]))
        answer_prods.append(cfg.Production(S, [D, D]))
        answer_prods.append(cfg.Production(D, [cfg.Epsilon()]))
        answer_wcnf = cfg.CFG({S}, {a, b, c, D}, S, set(answer_prods))
        return test_cfg, answer_wcnf
