from pyformlang.cfg import Production, Variable, Terminal, CFG, Epsilon
from project.ecfg import ECFG
from pyformlang.regular_expression import Regex
from functools import reduce


def equals_productions(fst_ecfg: ECFG, snd_ecfg: ECFG) -> bool:
    equal = True
    for k, v in fst_ecfg.productions.items():
        if k in snd_ecfg.productions:
            equal &= snd_ecfg.productions[k].head.value == v.head.value
            equal &= [x.head.value for x in snd_ecfg.productions[k].sons] == [
                x.head.value for x in v.sons
            ]
    return equal


def equals(fst_ecfg: ECFG, snd_ecfg: ECFG) -> bool:
    return (
        fst_ecfg.variables == snd_ecfg.variables
        and fst_ecfg.start_symbol == snd_ecfg.start_symbol
        and equals_productions(fst_ecfg, snd_ecfg)
    )


class TestEcfg:
    def test_from_cfg(self):
        ecfg = ECFG.from_cfg(self.cfg())
        assert equals(ecfg, self.ecfg_answer())

    def test_from_str(self):
        assert equals_productions(self.cfg_from_str(), self.cfg())

    def cfg(self):
        S = Variable("S")
        A = Variable("A")
        a = Terminal("a")
        b = Terminal("b")
        prods = []
        prods.append(Production(A, [S]))
        prods.append(Production(S, [A, S, A]))
        return CFG(
            {S, A},
            {a, b},
            S,
            set(prods),
        )

    def ecfg_answer(self):
        S = Variable("S")
        A = Variable("A")
        a = Terminal("a")
        b = Terminal("b")
        prods = {}
        prods[S] = reduce(Regex.concatenate, map(lambda x: Regex(x.value), [A, S, A]))
        prods[A] = reduce(Regex.concatenate, map(lambda x: Regex(x.value), [S]))
        return ECFG({A, S}, {a, b}, S, prods)

    def cfg_from_str(self):
        return ECFG.from_str(
            """
            S->A.S.A
            A->S
            """
        )
