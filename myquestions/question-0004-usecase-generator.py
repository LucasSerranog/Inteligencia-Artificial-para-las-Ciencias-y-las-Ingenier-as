import numpy as np
import random
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.datasets import make_classification

def generar_caso_de_uso_clasificar_knn():
    n_samples = random.randint(80, 150)
    n_features = random.randint(2, 5)
    k = random.randint(3, 7)
    
    X, y = make_classification(n_samples=n_samples, n_features=n_features,
                                n_informative=n_features, n_redundant=0,
                                random_state=random.randint(0, 100))
    
    split = int(n_samples * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]
    
    input_data = {
        "X_train": X_train,
        "y_train": y_train,
        "X_test": X_test,
        "y_test": y_test,
        "k": k
    }
    
    modelo = KNeighborsClassifier(n_neighbors=k)
    modelo.fit(X_train, y_train)
    preds = modelo.predict(X_test)
    
    output_data = {
        "accuracy": accuracy_score(y_test, preds),
        "precision": precision_score(y_test, preds, zero_division=0),
        "recall": recall_score(y_test, preds, zero_division=0),
        "f1_score": f1_score(y_test, preds, zero_division=0)
    }
    
    return input_data, output_data
```

---

### `myanswers/.gitkeep`
```
(vacío)
