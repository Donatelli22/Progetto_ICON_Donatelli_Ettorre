import graphviz as graphviz

def transformDataset(food):

    #cambio gli elementi vuoti di Costo e Diete
    food['Costo'].fillna('0', inplace=True)
    food['Diete'].fillna('Nessuna;', inplace=True)

    #Rimuovo il Nome dei piatti
    food.drop("Nome", inplace=True, axis=1)

    #Estaggo gli ingredienti
    lista = food["Ingredienti"]

    #Conto il numero di ingredienti per piatto
    ingredienti = []
    numIngredienti = []

    for i in range(len(lista)):
        ingredienti.append(lista[i])

    for i in range(len(ingredienti)):
        appoggio = str(ingredienti[i]).split(";")
        numIngredienti.append(len(set(appoggio)))

    #Inserisco il numero di ingredienti nel dataset
    for i in range(len(numIngredienti)):
        food.loc[i, "NumIngredienti"] = numIngredienti[i]

    #Rimuovo la colonna degli ingredienti
    food.drop("Ingredienti", inplace=True, axis=1)

    #Cambio le difficoltà in: Molto facile = 0; Facile = 1; Media = 2; Difficile = 3; Molto difficile = 4
    food.loc[food['Difficolta'] == 'Molto facile', 'Difficolta'] = '0'
    food.loc[food['Difficolta'] == 'Facile', 'Difficolta'] = '1'
    food.loc[food['Difficolta'] == 'Media', 'Difficolta'] = '2'
    food.loc[food['Difficolta'] == 'Difficile', 'Difficolta'] = '3'
    food.loc[food['Difficolta'] == 'Molto difficile', 'Difficolta'] = '4'

    #Cambio il costo in: Molto basso = 1; Basso = 2; Medio = 3; Alto = 4; Elevato = 5; Molto elevata = 6
    food.loc[food['Costo'] == 'Molto basso', 'Costo'] = '1'
    food.loc[food['Costo'] == 'Basso', 'Costo'] = '2'
    food.loc[food['Costo'] == 'Medio', 'Costo'] = '3'
    food.loc[food['Costo'] == 'Alto', 'Costo'] = '4'
    food.loc[food['Costo'] == 'Elevato', 'Costo'] = '5'
    food.loc[food['Costo'] == 'Molto elevata', 'Costo'] = '6'

    #Modifico il dataset aggiungendo una colonna per ogni dieta e assegnando 1 se quel piatto segue quella dieta, altrimenti 0
    #Light; Vegetariano; Sensa glutine; Senza lattosio; Nessuna;
    food.loc[food['Diete'].str.contains('Nessuna'), 'Dieta_Nessuna'] = '1'
    food.loc[~food['Diete'].str.contains('Nessuna'), 'Dieta_Nessuna'] = '0'
    food.loc[food['Diete'].str.contains('Light'), 'Dieta_Light'] = '1'
    food.loc[~food['Diete'].str.contains('Light'), 'Dieta_Light'] = '0'
    food.loc[food['Diete'].str.contains('Vegetariano'), 'Dieta_Vegetariano'] = '1'
    food.loc[~food['Diete'].str.contains('Vegetariano'), 'Dieta_Vegetariano'] = '0'
    food.loc[food['Diete'].str.contains('Senza lattosio'), 'Dieta_NoLattosio'] = '1'
    food.loc[~food['Diete'].str.contains('Senza lattosio'), 'Dieta_NoLattosio'] = '0'
    food.loc[food['Diete'].str.contains('Senza glutine'), 'Dieta_NoGlutine'] = '1'
    food.loc[~food['Diete'].str.contains('Senza glutine'), 'Dieta_NoGlutine'] = '0'

    #Rimuovo la colonna con le diete
    food.drop("Diete", inplace=True, axis=1)
    food.dropna(inplace=True)

    return food

def stringToInt(food):
    food['Difficolta'] = food['Difficolta'].astype(int)
    food['Costo'] = food['Costo'].astype(int)
    food['NumIngredienti'] = food['NumIngredienti'].astype(int)
    food['Dieta_Nessuna'] = food['Dieta_Nessuna'].astype(int)
    food['Dieta_Light'] = food['Dieta_Light'].astype(int)
    food['Dieta_Vegetariano'] = food['Dieta_Vegetariano'].astype(int)
    food['Dieta_NoLattosio'] = food['Dieta_NoLattosio'].astype(int)
    food['Dieta_NoGlutine'] = food['Dieta_NoGlutine'].astype(int)
    return food

def modForKNN(food):
    food.drop('Dieta_Nessuna', inplace=True, axis=1)
    food.drop('Dieta_Light', inplace=True, axis=1)
    food.drop('Dieta_Vegetariano', inplace=True, axis=1)
    food.drop('Dieta_NoLattosio', inplace=True, axis=1)
    food.drop('Dieta_NoGlutine', inplace=True, axis=1)
    return food