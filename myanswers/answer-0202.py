import pandas as pd

def calcular_rotacion_inventario(df):

    # Copiar el dataframe
    resultado = df.copy()

    # Calcular stock final
    stock_final = resultado['initial_stock'] - resultado['units_sold'] + resultado['restock_units']
    resultado['final_stock'] = stock_final

    # Calcular promedio de inventario
    promedio = (resultado['initial_stock'] + resultado['final_stock']) / 2

    # Calcular turnover_rate evitando division por cero
    tasa = []
    for i in range(len(resultado)):
        if promedio.iloc[i] == 0:
            tasa.append(0)
        else:
            tasa.append(resultado['units_sold'].iloc[i] / promedio.iloc[i])

    resultado['turnover_rate'] = tasa

    # Ordenar de mayor a menor y resetear indice
    resultado = resultado.sort_values('turnover_rate', ascending=False)
    resultado = resultado.reset_index(drop=True)

    return resultado
