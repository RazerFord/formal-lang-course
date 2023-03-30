from pyformlang import cfg
from pathlib import Path


def cfg_to_wcnf(cfg_gr: cfg.CFG) -> cfg.CFG:
    cfg_clear = (
        cfg_gr.remove_useless_symbols()
        .eliminate_unit_productions()
        .remove_useless_symbols()
    )

    prods = cfg_clear._get_productions_with_only_single_terminals()
    prods = cfg_clear._decompose_productions(prods)
    return cfg.CFG(start_symbol=cfg_clear.start_symbol, productions=set(prods))


def read_cfg_from_file(file: str, start: cfg.Variable = None) -> cfg.CFG:
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
    return cfg_to_wcnf(read_cfg_from_file(file, start))
