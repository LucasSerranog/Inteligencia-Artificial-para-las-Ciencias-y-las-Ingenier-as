import pandas as pd
import numpy as np

def calcular_rotacion_inventario(*args, **kwargs):
    # Acepta cualquier forma de llamado
    if args:
        arg = args[0]
        df = arg["df"] if isinstance(arg, dict) else arg
    elif "input" in kwargs:
        df = kwargs["input"]["df"]
    elif "df" in kwargs:
        df = kwargs["df"]

    res = df.copy()
    res['final_stock']   = res['initial_stock'] - res['units_sold'] + res['restock_units']
    avg_stock            = (res['initial_stock'] + res['final_stock']) / 2
    res['turnover_rate'] = np.where(avg_stock == 0, 0, res['units_sold'] / avg_stock)
    res = res.sort_values('turnover_rate', ascending=False).reset_index(drop=True)
    return res
