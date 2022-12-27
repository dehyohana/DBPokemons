import os
from webscraping import Scrapper
from sqlalchemy import create_engine

# Crio conexão banco de dados MySQL
connection = create_engine(
    'mysql+mysqlconnector://{}:{}@{}/{}'.format(
        os.environ.get("MYSQL_USER"),
        os.environ.get("MYSQL_PASSWORD"),
        os.environ.get("MYSQL_ADDRESS"),
        os.environ.get("MYSQL_DATABASE")
    )
)

scrap = Scrapper()
df = scrap.scrapping_pokemon()
df.to_sql(con = connection, name = "pokemon", if_exists="replace", index=False)