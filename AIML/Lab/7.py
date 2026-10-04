import numpy as np 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from collections import Counter 
 
# Load data 
X, y = load_iris(return_X_y=True) 
 
# Train-test split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 
 
class KNN: 
    def __init__(self, k=3): 
        self.k = k 
 
    def fit(self, X, y): 
        self.X = X 
        self.y = y 
 
    def predict(self, X_test): 
        predictions = [] 
        for x in X_test: 
            # Compute distances 
            distances = [np.linalg.norm(x - x_train) for x_train in self.X] 
            # Get k nearest labels 
            k_labels = [self.y[i] for i in np.argsort(distances)[:self.k]] 
            # Majority vote 
            predictions.append(Counter(k_labels).most_common(1)[0][0]) 
        return np.array(predictions) 
 
# Train and predict 
knn = KNN(k=3) 
knn.fit(X_train, y_train) 
y_pred = knn.predict(X_test) 
 
# Accuracy 
print("Accuracy:", np.mean(y_pred == y_test)) 