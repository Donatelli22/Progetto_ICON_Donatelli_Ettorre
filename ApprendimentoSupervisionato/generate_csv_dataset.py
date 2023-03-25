import csv
import json
import os
import sys


def delete_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')


file_count = len(os.listdir('C:/Users/Mattia/Desktop/Progetto ICON/GialloZafferano/Dataset'))
dir_name = 'dataset'

try:
    os.mkdir(dir_name)
except FileExistsError:
    pass

with open('gz_dataset.csv', mode='w+') as fp:
    fp_csv = csv.writer(fp, delimiter='|')
    fp_csv.writerow(['title', 'Difficolta', 'Costo', 'Diete', 'ingredients'])

    for i in range(file_count):
        delete_last_line()
        print(f'Processing {i} of {file_count} - {round(i/file_count*100,2)}% done.')
        filename = 'C:/Users/Mattia/Desktop/Progetto ICON/GialloZafferano/Dataset/gzd'+str(i)+'.json'
        with open(filename, 'r', encoding='utf-8') as json_in:
            recipe = json.loads(json_in.read())
            gz_title = recipe['Nome']
            gz_difficolta = recipe['Difficolta']
            gz_costo = recipe['Costo']
            gz_diete = ''
            for j in range(len(recipe['Diete'])):
                gz_diete += f"{recipe['Diete'][j]['dieta']}"
                gz_diete += "; "
            gz_ingredients = ''
            for j in range(len(recipe['Ingredienti'])):
                gz_ingredients += f"{recipe['Ingredienti'][j]['ingrediente']}"
                gz_ingredients += "; "
            #gz_preparation = recipe['preparation']
            fp_csv.writerow([gz_title, gz_difficolta, gz_costo, gz_diete, gz_ingredients])
    print(f'Done processing {file_count} files')