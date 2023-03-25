import graphviz as graphviz
import pandas as pd
import matplotlib.pyplot as plt
import transformDataset as tr

# carico il dataset
food = pd.read_csv("./gz_dataset.csv", sep='|', encoding='latin-1')

foodModifie = tr.transformDataset(food)
foodModifie = tr.stringToInt(foodModifie)

foodModifie["Difficolta"].hist()
plt.show()

correlation_matrix = foodModifie.corr()
print(correlation_matrix['Difficolta'])
