import numpy as np
import random
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

def generar_caso_de_uso_pipeline_pca_regresion():
    n_samples = random.randint(50, 100)
    n_features = random.randint(5, 10)
    n_components = random.randint(2, min(4, n_features - 1))
    
    X = np.random.randn(n_samples, n_features)
    y = np.random.randn(n_samples)
    
    split = int(n_samples * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train = y[:split]
    
    input_data = {
        "X_train": X_train,
        "y_train": y_train,
        "X_test": X_test,
        "n_components": n_components
    }
    
    pipeline = Pipeline([
        ("pca", PCA(n_components=n_components)),
        ("regresion", LinearRegression())
    ])
    pipeline.fit(X_train, y_train)
    output_data = pipeline.predict(X_test)
    
    return input_data, output_data
