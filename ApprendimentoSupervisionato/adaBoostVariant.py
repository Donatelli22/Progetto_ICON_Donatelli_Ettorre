import numpy as np
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import r2_score
import transformDataset as tr
import matplotlib.pyplot as plt

#Carico il dataset
food = pd.read_csv("./gz_dataset.csv", sep='|', encoding='latin-1')

#Modifico il dataset
foodModifie = tr.transformDataset(food)

#Creo i dataset delle proprietà X e del target Y
X = foodModifie.drop("Difficolta", axis=1).values
Y = foodModifie["Difficolta"].values

X_col = foodModifie.drop("Difficolta", axis=1)
Y_col = foodModifie["Difficolta"]

#Suddivido il dataset in dataset di train e di test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=5)

max_tree = 30

max_tree_range = list(range(1, max_tree))
accuracy_test = []
accuracy_train = []
sommaData = []
sommaRquadro = 0
sommaSquareError = 0
importances = []

for tree in max_tree_range:    
    adaBoost = AdaBoostClassifier(n_estimators=tree, random_state = 5)
    adaBoost.fit(X_train, Y_train)
    Y_pred_train = adaBoost.predict(X_train)
    Y_pred_test = adaBoost.predict(X_test)

    score_train = accuracy_score(Y_train, Y_pred_train)
    accuracy_train.append(score_train)

    score_test = accuracy_score(Y_test, Y_pred_test)
    accuracy_test.append(score_test)

    sommaRquadro += r2_score(Y_test, Y_pred_test)
    sommaSquareError += metrics.mean_squared_error(Y_test, Y_pred_test)
    sommaData += precision_recall_fscore_support(Y_test, Y_pred_test, average='macro', labels=np.unique(Y_pred_test))
    importances.append(pd.DataFrame({'importance':np.round(adaBoost.feature_importances_,5)}, index=X_col.columns))

importance = 0
for i in range(len(importances)):
    importance = importance + (importances[i])
importance = importance/max_tree

Accuracy = sum(accuracy_test)/max_tree
Rquadro = sommaRquadro / max_tree
SquareError = sommaSquareError / max_tree
Precision = sommaData[0] / max_tree
Recall = sommaData[1] / max_tree
f1 = sommaData[2] / max_tree

print('Accuracy: ', Accuracy)
print('R-quadrato: ', Rquadro)
print('Errore quadratico medio: ', SquareError)
print('Precisione: ', Precision)
print('Richiamo: ', Recall)
print('F1: ', f1)
print(importance)

plt.plot(range(1, max_tree), accuracy_train, label = "Training Score")
plt.plot(range(1, max_tree), accuracy_test, label = "Test Score")
plt.xlabel('Number of Trees')
plt.ylabel('Scores')
plt.legend()
plt.show()