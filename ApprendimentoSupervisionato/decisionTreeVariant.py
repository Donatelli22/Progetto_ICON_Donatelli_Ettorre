import graphviz as graphviz
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, r2_score, precision_recall_fscore_support
from sklearn.model_selection import train_test_split, KFold
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import metrics 
import transformDataset as tr
import matplotlib.pyplot as plt

# carico il dataset
food = pd.read_csv("./gz_dataset.csv", sep='|', encoding='latin-1')

#Modifico il dataset
foodModifie = tr.transformDataset(food)

# creo i dataset delle proprietà X e del target Y
X = foodModifie.drop("Difficolta", axis=1).values
Y = foodModifie["Difficolta"].values

X_col = foodModifie.drop("Difficolta", axis=1)
Y_col = foodModifie["Difficolta"]

# suddivido il dataset in dataset di train e di test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

max_depth = 30

#vediamo il variare dell'accuratezza al variare della massima profondità
max_depth_range = list(range(1, max_depth))
accuracy_test = []
accuracy_train = []
sommaData = []
sommaRquadro = 0
sommaSquareError = 0
importances = []

for depth in max_depth_range:    
    decTree = DecisionTreeClassifier(max_depth = depth, random_state = 0, criterion="gini")
    decTree.fit(X_train, Y_train)

    Y_pred_train = decTree.predict(X_train)
    Y_pred_test = decTree.predict(X_test)

    score_train = accuracy_score(Y_train, Y_pred_train)
    accuracy_train.append(score_train)

    score_test = accuracy_score(Y_test, Y_pred_test)
    accuracy_test.append(score_test)

    sommaRquadro += r2_score(Y_test, Y_pred_test)
    sommaSquareError += metrics.mean_squared_error(Y_test, Y_pred_test)
    sommaData += precision_recall_fscore_support(Y_test, Y_pred_test, average='macro', labels=np.unique(Y_pred_test))
    importances.append(pd.DataFrame({'importance':np.round(decTree.feature_importances_,5)}, index=X_col.columns))

    if depth == 3:
        dot_data = export_graphviz(decTree, out_file=None, feature_names=foodModifie.columns.drop("Difficolta"))
        graph = graphviz.Source(dot_data)
        graph.render("liver_tree_gini", view=True)

importance = 0
for i in range(len(importances)):
    importance = importance+(importances[i])
importance = importance/max_depth

Accuracy = sum(accuracy_test)/max_depth
Rquadro = sommaRquadro / max_depth
SquareError = sommaSquareError / max_depth
Precision = sommaData[0] / max_depth
Recall = sommaData[1] / max_depth
f1 = sommaData[2] / max_depth

print('Accuracy: ', Accuracy)
print('R-quadrato: ', Rquadro)
print('Errore quadratico medio: ', SquareError)
print('Precisione: ', Precision)
print('Richiamo: ', Recall)
print('F1: ', f1)
print(importance)

plt.plot(range(1, max_depth), accuracy_train, label = "Training Score")
plt.plot(range(1, max_depth), accuracy_test, label = "Test Score")
plt.xlabel('Tree Depth')
plt.ylabel('Scores')
plt.legend()
#plt.show()