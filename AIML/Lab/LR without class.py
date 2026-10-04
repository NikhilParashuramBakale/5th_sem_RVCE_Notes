import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# ---------------- LOAD DATA ----------------
iris = datasets.load_iris()
x = iris.data[:, :2]                  # first two features
y = (iris.target != 0) * 1            # binary classification

# ---------------- FEATURE SCALING ----------------
sc = StandardScaler()
x = sc.fit_transform(x)

# ---------------- TRAIN TEST SPLIT ----------------
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.4, random_state=42
)

# ---------------- LOGISTIC REGRESSION FUNCTIONS ----------------
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def gradient(x, h, y):
    return np.dot(x.T, (h - y)) / y.shape[0]

def train_logistic_regression(x, y, learning_rate=0.01, num_iterations=200):
    weights = np.zeros(x.shape[1])

    for _ in range(num_iterations):
        z = np.dot(x, weights)
        h = sigmoid(z)
        grad = gradient(x, h, y)
        weights = weights - learning_rate * grad

    return weights

def predict(x, weights):
    z = np.dot(x, weights)
    return (sigmoid(z) > 0.5) * 1

# ---------------- TRAIN MODEL ----------------
weights = train_logistic_regression(
    x_train, y_train, learning_rate=0.01, num_iterations=200
)

# ---------------- TEST MODEL ----------------
y_pred = predict(x_test, weights)
accuracy = np.mean(y_pred == y_test)
print("Accuracy:", accuracy)

# ---------------- VISUALIZATION ----------------
plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train)
plt.title("Logistic Regression (Without Class)")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.show()
