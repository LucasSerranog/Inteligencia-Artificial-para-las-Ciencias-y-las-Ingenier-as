import pandas as pd
import numpy as np

def calcular_rotacion_inventario(df=None, input=None, output=None):
    if df is None and input is not None:
        df = input["df"]
    df = df.copy()
    df['final_stock'] = df['initial_stock'] - df['units_sold'] + df['restock_units']
    avg_stock = (df['initial_stock'] + df['final_stock']) / 2
    df['turnover_rate'] = np.where(avg_stock == 0, 0, df['units_sold'] / avg_stock)
    df = df.sort_values('turnover_rate', ascending=False).reset_index(drop=True)
    return df
