from project.ecfg import ECFG
from pyformlang.cfg import Variable, CFG
from pyformlang.regular_expression import Regex


class TestRsm:
    def test_ecfg_to_rsm(self):
        txt = """
            S->A.S.A
            A->S
            """
        ecfg = ECFG.from_str(txt)
        rsm = ecfg.to_rsm().minimize()
        assert rsm.boxes["S"] == Regex("A.S.A").to_epsilon_nfa().minimize()
        assert rsm.boxes["A"] == Regex("S").to_epsilon_nfa().minimize()

    def test_ecfg_to_rsm_concatenate(self):
        txt = """
            S->A.S.A
            S->B.A
            A->S
            """
        ecfg = ECFG.from_str(txt)
        rsm = ecfg.to_rsm().minimize()
        assert rsm.boxes["S"] == Regex("A.S.A|B.A").to_epsilon_nfa().minimize()
        assert rsm.boxes["A"] == Regex("S").to_epsilon_nfa().minimize()
