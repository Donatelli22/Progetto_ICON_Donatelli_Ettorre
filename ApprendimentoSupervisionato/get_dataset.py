from get_recipes import Recipe
import json
import sys


def delete_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')


links = json.loads(open('gz_links.json', mode='r', encoding='utf-8').read())
n_links = len(links)
for i in range(n_links):
        delete_last_line()
        print(f'Getting {i} of {n_links} - {round(i/n_links*100,2)}% done.')
        filename = f'C:/Users/Mattia/Desktop/Progetto ICON/GialloZafferano/Dataset/gzd{str(i)}.json'
        with open(filename, mode='w', encoding='utf-8') as fp:
                R = Recipe(links[i]).get()
                json.dump(R, fp, indent=4, sort_keys=False, ensure_ascii=False)
print(f'Done getting all {n_links} recipes.')