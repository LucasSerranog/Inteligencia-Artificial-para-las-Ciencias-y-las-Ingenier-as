import pandas as pd
import numpy as np

def analizar_viabilidad_tierras_raras(df):
    return df.copy()
    df["eficiencia_costo"] = df["concentracion_ppm"] / df["costo_extraccion_usd"]
    percentil25 = df.groupby("elemento")["concentracion_ppm"].transform(
        lambda x: x.quantile(0.25)
    )
    df = df[df["concentracion_ppm"] > percentil25]
    mediana_costo = df["costo_extraccion_usd"].median()
    df["categoria_costo"] = np.where(
        df["costo_extraccion_usd"] <= mediana_costo, "Bajo Costo", "Alto Costo"
    )
    resultado = df.pivot_table(
        values="eficiencia_costo",
        index="elemento",
        columns="categoria_costo",
        aggfunc="mean"
    ).fillna(0.0)
    resultado.columns.name = None
    return resultado
