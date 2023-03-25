import graphviz as graphviz
import pandas as pd
import matplotlib.pyplot as plt
import transformDataset as tr
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, precision_recall_fscore_support
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

# carico il dataset
food = pd.read_csv("./gz_dataset.csv", sep='|', encoding='latin-1')

#modifico il dataset in uno totalmente numerico
foodModifie = tr.transformDataset(food)
foodModifie = tr.stringToInt(foodModifie)
foodModifie =tr.modForKNN(foodModifie)

# creo i dataset delle proprietà X e del target Y
X = foodModifie.drop("Difficolta", axis=1).values
Y = foodModifie['Difficolta'].values

# suddivido il dataset in dataset di train e di test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

#definisco il numero massimo di vicini
max_k = 50

max_k_range = list(range(1, max_k))
k_scores = []
test_accuracy = []
train_accuracy = []
sommaData = []
sommaRquadro = 0
sommaSquareError = 0

#calcoliamo i modelli al variare del numero dei vicini
for depth in max_k_range:
    knn_model = KNeighborsClassifier(n_neighbors=depth)
    knn_model.fit(X_train, Y_train)
    
    Y_pred_train = knn_model.predict(X_train)
    Y_pred_test = knn_model.predict(X_test)

    train_accuracy.append(knn_model.score(X_train, Y_train))
    test_accuracy.append(knn_model.score(X_test, Y_test))

    sommaRquadro += r2_score(Y_test, Y_pred_test)
    sommaData += precision_recall_fscore_support(Y_test, Y_pred_test, average="macro", labels=np.unique(Y_pred_test))

# stampo i risultati
print('Accuracy: ', sum(train_accuracy)/max_k)
print('Precision: ', sommaData[0]/max_k)
print('Recall: ', sommaData[1]/max_k)
print('F1: ', sommaData[2]/max_k)

#metto su un grafico gli score
plt.plot(range(1, max_k), test_accuracy, label = 'Test accuracy')
plt.plot(range(1,max_k), train_accuracy, label = 'Train accuracy')
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross_validated Accuracy')
plt.legend()
plt.show()

# metto in un grafo i valori delle due colonne
cmap = sns.cubehelix_palette(as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(X_test[:, 0], X_test[:, 1], c=Y_test, s=50, cmap=cmap)
f.colorbar(points)
plt.show()
