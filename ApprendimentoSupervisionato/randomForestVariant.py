import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
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
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

max_depth = 30

#vediamo il variare dell'accuratezza al variare della massima profondità
max_depth_range = list(range(1, max_depth))
accuracy_test = []
accuracy_train = []
sommaData = []
sommaRquadro = 0
sommaSquareError = 0
importances_deep = []

for depth in max_depth_range:    
    randTree = RandomForestClassifier(max_depth = depth, random_state = 0, criterion="gini")
    randTree.fit(X_train, Y_train)
    Y_pred_train = randTree.predict(X_train)
    Y_pred_test = randTree.predict(X_test)

    score_train = accuracy_score(Y_train, Y_pred_train)
    accuracy_train.append(score_train)

    score_test = accuracy_score(Y_test, Y_pred_test)
    accuracy_test.append(score_test)

    sommaRquadro += r2_score(Y_test, Y_pred_test)
    sommaSquareError += metrics.mean_squared_error(Y_test, Y_pred_test)
    sommaData += precision_recall_fscore_support(Y_test, Y_pred_test, average='macro', labels=np.unique(Y_pred_test))
    importances_deep.append(pd.DataFrame({'importance':np.round(randTree.feature_importances_,5)}, index=X_col.columns))

importance_deep = 0
for i in range(len(importances_deep)):
    importance_deep = importance_deep + (importances_deep[i])
importance_deep = importance_deep/max_depth

Accuracy = sum(accuracy_test)/max_depth
Rquadro = sommaRquadro / max_depth
SquareError = sommaSquareError / max_depth
Precision = sommaData[0] / max_depth
Recall = sommaData[1] / max_depth
f1 = sommaData[2] / max_depth

print('Depth variant: ')
print('Accuracy: ', Accuracy)
print('R-quadrato: ', Rquadro)
print('Errore quadratico medio: ', SquareError)
print('Precisione: ', Precision)
print('Richiamo: ', Recall)
print('F1: ', f1)

plt.plot(range(1, max_depth), accuracy_train, label = "Training Score")
plt.plot(range(1, max_depth), accuracy_test, label = "Test Score")
plt.xlabel('Tree Depth')
plt.ylabel('Scores')
plt.legend()
plt.show()

#
# 
# 
#

max_tree = 30

max_tree_range = list(range(1, max_tree))
accuracy_test = []
accuracy_train = []
sommaData = []
sommaRquadro = 0
sommaSquareError = 0
importances_tree = []

for tree in max_tree_range:    
    randTree = RandomForestClassifier(max_depth=15, n_estimators=tree, random_state = 0, criterion="gini")
    randTree.fit(X_train, Y_train)
    Y_pred_train = randTree.predict(X_train)
    Y_pred_test = randTree.predict(X_test)

    score_train = accuracy_score(Y_train, Y_pred_train)
    accuracy_train.append(score_train)

    score_test = accuracy_score(Y_test, Y_pred_test)
    accuracy_test.append(score_test)

    sommaRquadro += r2_score(Y_test, Y_pred_test)
    sommaSquareError += metrics.mean_squared_error(Y_test, Y_pred_test)
    sommaData += precision_recall_fscore_support(Y_test, Y_pred_test, average='macro', labels=np.unique(Y_pred_test))
    importances_tree.append(pd.DataFrame({'importance':np.round(randTree.feature_importances_,5)}, index=X_col.columns))

importance_tree = 0
for i in range(len(importances_tree)):
    importance_tree = importance_tree + (importances_tree[i])
importance_tree = importance_tree/max_depth

Accuracy = sum(accuracy_test)/max_depth
Rquadro = sommaRquadro / max_tree
SquareError = sommaSquareError / max_tree
Precision = sommaData[0] / max_tree
Recall = sommaData[1] / max_tree
f1 = sommaData[2] / max_tree

print('Tree variant: ')
print('Accuracy: ', Accuracy)
print('R-quadrato: ', Rquadro)
print('Errore quadratico medio: ', SquareError)
print('Precisione: ', Precision)
print('Richiamo: ', Recall)
print('F1: ', f1)

importance = importance_tree + importance_deep
importance = importance/2

print(importance)
plt.plot(range(1, max_tree), accuracy_train, label = "Training Score")
plt.plot(range(1, max_tree), accuracy_test, label = "Test Score")
plt.xlabel('Number of Trees')
plt.ylabel('Scores')
plt.legend()
plt.show()