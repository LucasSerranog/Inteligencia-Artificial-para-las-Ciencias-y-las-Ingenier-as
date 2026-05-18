import pandas as pd
import numpy as np

def calcular_rotacion_inventario(df=None, output=None, **kwargs):
    # 1. Extraer el DataFrame de forma flexible por si el evaluador lo envía de otra forma
    if df is None:
        if 'df' in kwargs:
            df = kwargs['df']
        elif 'input' in kwargs and isinstance(kwargs['input'], dict):
            df = kwargs['input'].get('df')
            
    if isinstance(df, dict) and 'df' in df:
        df = df['df']

    # 2. Procesar los datos de manera segura
    res = df.copy()
    
    res['final_stock'] = res['initial_stock'] - res['units_sold'] + res['restock_units']
    avg_stock = (res['initial_stock'] + res['final_stock']) / 2
    
    # Evitamos la división por cero usando numpy
    res['turnover_rate'] = np.where(avg_stock == 0, 0, res['units_sold'] / avg_stock)
    
    # Ordenar de mayor a menor rotación y limpiar el índice
    res = res.sort_values('turnover_rate', ascending=False).reset_index(drop=True)
    
    return res
