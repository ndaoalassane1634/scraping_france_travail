import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = "https://candidat.francetravail.fr/offres/recherche?lieux=69381&motsCles=data&natureOffre=E2&offresPartenaires=true&range=0-19&rayon=10&tri=0"
page = requests.get(url)

soup = bs(page.content, 'html.parser')
soup

#creation du valeur mere
france_travail = soup.find_all("li" , class_="result")
france_travail

#creation de variable secondaire
titles_clean = []
adress_clean = []
description_clean = []
type_contrat_clean  = []

#CREATION DES BOUCLES
for france_travail in france_travails :
    france_travail.find("span", class_="media-heading-title").text
    titles_clean.append(france_travail.find("span", class_="media-heading-title").text)

    france_travail.find('p', class_="subtext").find("span").text
    adress_clean.append(france_travail.find('p', class_="subtext").find("span").text)

    france_travail.find('p', class_="description").text
    description_clean.append(france_travail.find('p' , class_="description").text)

    france_travail.find('p', class_="contrat visible-xs").text
    type_contrat_clean.append(france_travail.find('p', class_="contrat visible-xs").text)

#ajout dataFrame
df = pd.DataFrame({"Poste" : titles_clean , "Entreprise" : adress_clean , "Description" : description_clean, "Contrat" : type_contrat_clean})
df
