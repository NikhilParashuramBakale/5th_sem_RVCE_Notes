import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# ---------------- NAIVE BAYES FUNCTIONS ----------------

def fit_naive_bayes(X, y):
    classes = np.unique(y)
    mean = np.array([X[y == c].mean(axis=0) for c in classes])
    var = np.array([X[y == c].var(axis=0) for c in classes])
    priors = np.array([X[y == c].shape[0] / len(y) for c in classes])
    return classes, mean, var, priors

def gaussian_pdf(class_idx, x, mean, var):
    numerator = np.exp(- (x - mean[class_idx])**2 / (2 * var[class_idx]))
    denominator = np.sqrt(2 * np.pi * var[class_idx])
    return numerator / denominator

def predict_sample(x, classes, mean, var, priors):
    posteriors = []
    for idx, prior in enumerate(priors):
        log_prior = np.log(prior)
        log_likelihood = np.sum(np.log(gaussian_pdf(idx, x, mean, var)))
        posteriors.append(log_prior + log_likelihood)
    return classes[np.argmax(posteriors)]

def predict(X, classes, mean, var, priors):
    return np.array([predict_sample(x, classes, mean, var, priors) for x in X])

# ---------------- TRAIN & TEST ----------------
    
classes, mean, var, priors = fit_naive_bayes(X_train, y_train)
y_pred = predict(X_test, classes, mean, var, priors)

# Accuracy
print("Accuracy:", np.mean(y_pred == y_test))

# Class names
print("Predictions:", class_names[y_pred])

# Confusion matrix & report
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))
