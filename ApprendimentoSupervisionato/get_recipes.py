import urllib3
from bs4 import BeautifulSoup
import codecs


class Recipe():
    def __init__(self, url):
        self.url = url

    def get(self):
        url = self.url
        http = urllib3.PoolManager()
        urllib3.disable_warnings()
        response = http.request('GET', url)
        html = codecs.decode(response.data, 'utf-8')
        soup = BeautifulSoup(html, 'lxml')

        # Title
        if soup.find('h1', class_='gz-title-recipe').text is not None:
            Rtitle = soup.find('h1', class_='gz-title-recipe').text

        #Difficoltà & Dieta
        x = 0
        feature = soup.find_all("span", class_='gz-name-featured-data')
        RDifficolta = feature[0].text
        Rcosto = None
        for i in range(len(feature)):
            x = x + 1
        if x > 4:
            Rcosto = feature[4].text

        #Diete
        diete = soup.find_all("span", class_='gz-name-featured-data-other')
        Rdiete = list(dict())
        for i in range(len(diete)):
            Rdiete.append({'dieta': diete[i].text})

        # Ingredienti
        ingredients = soup.find_all('dd', class_='gz-ingredient')
        Ringredients = list(dict())
        for i in range(len(ingredients)):
            Ringredients.append({'ingrediente': ingredients[i].a.text})
        Recipe = {'Nome': Rtitle, 'Difficolta': RDifficolta, 'Costo': Rcosto, 'Diete': Rdiete, 'Ingredienti': Ringredients}
        return Recipe