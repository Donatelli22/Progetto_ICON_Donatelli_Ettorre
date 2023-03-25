from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd
import transformDataset as tr
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

#Carico il dataset
food = pd.read_csv("./gz_dataset.csv", sep='|', encoding='latin-1')

#Modifico il dataset
foodModifie = tr.transformDataset(food)
foodModifie = tr.modForKNN(foodModifie)

#Creo i dataset delle proprietà X e del target Y
X = foodModifie.drop("Difficolta", axis=1).values
Y = foodModifie["Difficolta"].values

#Suddivido il dataset in dataset di train e di test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

model = GaussianNB()
model.fit(X_train, Y_train)

Y_pred_test = model.predict(X_test)
Y_pred_train = model.predict(X_train)

data = []
accuracy_train = accuracy_score(Y_pred_train, Y_train)
accuracy_test = accuracy_score(Y_pred_test, Y_test)
data = precision_recall_fscore_support(Y_test, Y_pred_test, average='macro',  labels=np.unique(Y_pred_test))

print('Accuracy test set: ', accuracy_test)
print('Accuracy train set: ', accuracy_train)
print('f1: ', data[2])
print('Precision: ', data[0])
print('Recall: ', data[1])