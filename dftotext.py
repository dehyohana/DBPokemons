import os
from webscraping import Scrapper

scrap = Scrapper()
df = scrap.scrapping_pokemon()
csv_data = df.to_csv("pokemons.csv", index=False)