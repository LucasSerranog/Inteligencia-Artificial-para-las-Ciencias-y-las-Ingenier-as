import pandas as pd
import numpy as np

def calcular_rotacion_inventario(df):
    res = df.copy()
    
    # 1. final_stock
    res['final_stock'] = res['initial_stock'] - res['units_sold'] + res['restock_units']
    
    # 2. promedio del inventario
    avg_stock = (res['initial_stock'] + res['final_stock']) / 2
    
    # 3. turnover_rate (0 si avg_stock == 0)
    res['turnover_rate'] = np.where(avg_stock == 0, 0, res['units_sold'] / avg_stock)
    
    # 4. ordenar de mayor a menor y resetear índice
    res = res.sort_values('turnover_rate', ascending=False).reset_index(drop=True)
    
    return res
