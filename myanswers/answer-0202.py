import pandas as pd
import numpy as np

def calcular_rotacion_inventario(df):

    # Paso 1: copiar el dataframe para no modificar el original
    resultado = df.copy()

    # Paso 2: calcular el stock final
    resultado['final_stock'] = resultado['initial_stock'] - resultado['units_sold'] + resultado['restock_units']

    # Paso 3: calcular el promedio del inventario
    resultado['avg_stock'] = (resultado['initial_stock'] + resultado['final_stock']) / 2

    # Paso 4: calcular turnover_rate fila por fila, evitando division por cero
    turnover = []

    for i in range(len(resultado)):
        avg = resultado['avg_stock'].iloc[i]
        sold = resultado['units_sold'].iloc[i]

        if avg == 0:
            turnover.append(0)
        else:
            turnover.append(sold / avg)

    resultado['turnover_rate'] = turnover

    # Paso 5: eliminar columna auxiliar avg_stock
    resultado = resultado.drop(columns=['avg_stock'])

    # Paso 6: ordenar de mayor a menor turnover_rate y resetear indice
    resultado = resultado.sort_values('turnover_rate', ascending=False)
    resultado = resultado.reset_index(drop=True)

    return resultado
