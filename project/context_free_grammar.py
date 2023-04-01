from pyformlang import cfg
from pathlib import Path


def cfg_to_wcnf(cfg_gr: cfg.CFG) -> cfg.CFG:
    """
    Parameters
    ----------
    cfg_gr : cfg_gr.CFG
        Context-free grammar for which we want to get Chomsky's weak
        normal form

    Returns
    ----------
    cfg.CFG
        A context-free grammar in weak Chomsky normal form
    """
    cfg_clear = cfg_gr.eliminate_unit_productions().remove_useless_symbols()

    prods = cfg_clear._get_productions_with_only_single_terminals()
    prods = cfg_clear._decompose_productions(prods)
    return cfg.CFG(start_symbol=cfg_clear.start_symbol, productions=set(prods))


def read_cfg_from_file(file: str, start: cfg.Variable = None) -> cfg.CFG:
    """
    Parameters
    ----------
    file : str
        The name of the file that contains the context-free grammar

    start : cfg.Variable
        Start variable in a context-free grammar

    Returns
    ----------
    cfg.CFG
        Returns a context-Free Grammar
    """
    if not Path(file).is_file():
        return None

    with open(file) as cin:
        text_cfg = "".join(cin.readlines())
    if start is None:
        cfg_res = cfg.CFG.from_text(text_cfg, cfg.Variable("S"))
    else:
        cfg_res = cfg.CFG.from_text(text_cfg, start)
    return cfg_res


def read_wcfg_from_file(file: str, start: cfg.Variable = None) -> cfg.CFG:
    """
    Parameters
    ----------
    file : str
        The name of the file that contains the context-free grammar

    start : cfg.Variable
        Start variable in a context-free grammar

    Returns
    ----------
    cfg.CFG
        Returns a context-free grammar in weak Chomsky normal form
    """
    return cfg_to_wcnf(read_cfg_from_file(file, start))
