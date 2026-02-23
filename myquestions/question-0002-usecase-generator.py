import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_combinar_ventas():
    n_productos = random.randint(5, 10)
    n_ventas = random.randint(10, 30)
    top_n = random.randint(2, n_productos)
    
    productos_ids = list(range(1, n_productos + 1))
    nombres = [f"Producto_{i}" for i in productos_ids]
    
    df_productos = pd.DataFrame({
        "producto_id": productos_ids,
        "nombre": nombres
    })
    
    df_ventas = pd.DataFrame({
        "producto_id": np.random.choice(productos_ids, size=n_ventas),
        "cantidad_vendida": np.random.randint(1, 100, size=n_ventas)
    })
    
    input_data = {
        "df_productos": df_productos.copy(),
        "df_ventas": df_ventas.copy(),
        "top_n": top_n
    }
    
    merged = df_productos.merge(df_ventas, on="producto_id")
    resultado = merged.groupby("nombre")["cantidad_vendida"].sum().reset_index()
    resultado = resultado.sort_values("cantidad_vendida", ascending=False).head(top_n).reset_index(drop=True)
    
    output_data = resultado
    
    return input_data, output_data
