import pandas as pd
import numpy as np

def priorizar_reabastecimiento(df, stock_umbral, demanda_umbral):
    df = df.copy()
    df = df[(df['stock_actual'] < stock_umbral) &
            (df['demanda_mensual'] > demanda_umbral)]
    if not df.empty:
        df['indice_prioridad'] = (df['demanda_mensual'] - df['stock_actual']) / df['demanda_mensual']
        df = df.sort_values(by='indice_prioridad', ascending=False).reset_index(drop=True)
    else:
        df = pd.DataFrame(columns=['producto', 'stock_actual', 'demanda_mensual', 'indice_prioridad'])
    return df
