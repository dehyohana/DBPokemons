from generation import Generation
from webscraping import Scrapper

generation = 1
pokemon_generation = Generation
poke_range = pokemon_generation.pokemon_range(pokemon_generation, generation)

scrap = Scrapper()
df = scrap.scrapping_pokemon(poke_range)
csv_data = df.to_csv("pokemon_gen1.csv", index=False)