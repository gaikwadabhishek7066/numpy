import numpy as np
from collections import Counter

def euclidean(a, b):
    return np.sqrt(np.sum((a - b)**2))

def knn_predict(X_train, y_train, X_test, k=3):
    preds = []
    for x in X_test:
        idx = np.argsort([euclidean(x, t) for t in X_train])[:k]
        label = Counter(y_train[idx]).most_common(1)[0][0]
        preds.append(label)
    return np.array(preds)

