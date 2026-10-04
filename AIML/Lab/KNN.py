import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from collections import Counter

# Load dataset
X, y = load_iris(return_X_y=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# ---------------- KNN FUNCTIONS ----------------

def knn_predict(X_train, y_train, X_test, k=3):
    predictions = []

    for x in X_test:
        # Compute distances to all training points
        distances = [np.linalg.norm(x - x_train) for x_train in X_train]

        # Get indices of k nearest neighbors
        k_indices = np.argsort(distances)[:k]

        # Get corresponding labels
        k_labels = [y_train[i] for i in k_indices]

        # Majority vote
        predictions.append(Counter(k_labels).most_common(1)[0][0])

    return np.array(predictions)

# ---------------- PREDICT & EVALUATE ----------------

y_pred = knn_predict(X_train, y_train, X_test, k=3)

print("Accuracy:", np.mean(y_pred == y_test))
