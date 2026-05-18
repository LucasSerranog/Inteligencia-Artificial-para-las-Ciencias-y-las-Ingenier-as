import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score

def evaluar_con_stratified_kfold(df, target_col):
    X = df.drop(columns=[target_col]).values
    y = df[target_col].values
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = []
    for train_idx, test_idx in skf.split(X, y):
        model = DecisionTreeClassifier(random_state=42)
        model.fit(X[train_idx], y[train_idx])
        y_pred = model.predict(X[test_idx])
        scores.append(accuracy_score(y[test_idx], y_pred))
    return np.mean(scores), np.std(scores)
