import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_calcular_media_movil():
    n_rows = random.randint(20, 50)
    ventana = random.randint(2, 5)

    fechas = pd.date_range("2020-01-01", periods=n_rows, freq="D")
    valores = np.random.randn(n_rows) * 10 + 30

    df = pd.DataFrame({"fecha": fechas, "valor": valores})

    input_data = {
        "df": df.copy(),
        "columna": "valor",
        "ventana": ventana
    }

    df["media_movil"] = df["valor"].rolling(window=ventana).mean()
    df = df.dropna().reset_index(drop=True)

    output_data = df

    return input_data, output_data

generar_caso_de_uso_calcular_media_movil()
