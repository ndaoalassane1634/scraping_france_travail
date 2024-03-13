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
