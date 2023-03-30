from pyformlang import cfg


def cfg_to_wcnf(cfg_gr: cfg.CFG):
    cfg_clear = (
        cfg_gr.remove_useless_symbols()
        .eliminate_unit_productions()
        .remove_useless_symbols()
    )

    prods = cfg_clear._get_productions_with_only_single_terminals()
    prods = cfg_clear._decompose_productions(prods)
    return cfg.CFG(start_symbol=cfg_clear.start_symbol, productions=set(prods))
