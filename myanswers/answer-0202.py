import pandas as pd
import numpy as np

def calcular_rotacion_inventario(*args, **kwargs):
    # Extrae df de donde sea que venga
    if args:
        arg = args[0]
        if isinstance(arg, dict):
            df = arg.get("df") or arg.get("input", {}).get("df")
        else:
            df = arg
    else:
        inp = kwargs.get("input") or kwargs.get("df") or kwargs
        df = inp.get("df") if isinstance(inp, dict) else inp

    res = df.copy()
    res['final_stock']   = res['initial_stock'] - res['units_sold'] + res['restock_units']
    avg_stock            = (res['initial_stock'] + res['final_stock']) / 2
    res['turnover_rate'] = np.where(avg_stock == 0, 0, res['units_sold'] / avg_stock)
    res = res.sort_values('turnover_rate', ascending=False).reset_index(drop=True)
    return res
