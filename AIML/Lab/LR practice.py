import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
iris=datasets.load_iris()
x=iris.data[:,:2]
y=(iris.target!=0)*1
sc=StandardScaler()
x=sc.fit_transform(x)
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
def gradient(x,h,y):
    return np.dot(x.T,(h-y))/y.shape[0]
def predict(x,weights):
    z=np.dot(x,weights)
    return (sigmoid(z)>0.5)*1
def train_logostic_regression(x,y,learning_rate=0.01,num_iterations=1000):
    weights=np.zeros(x.shape[1])
    for i in range(num_iterations):
        z=np.dot(x,weights)
        h=sigmoid(z)
        grad=gradient(x,h,y)
        weights-=learning_rate*grad
    return weights

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

weights=train_logostic_regression(x_train,y_train,learning_rate=0.1,num_iterations=1000)
ypred=predict(x_test,weights)
accuracy=np.mean(ypred==y_test)
print(f'Accuracy: {accuracy*100}%')



