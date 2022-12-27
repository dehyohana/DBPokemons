from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

class Scrapper:
    def __init__(self) -> None:
        self.url = "https://pokemondb.net/pokedex/national"

    def __get_id__(self, soup: bs) -> list:
        """Return id list
        Args:
            soup (bs): BeautifulSoup
        Returns:
            list: id_list[int]
        """
        id_list = soup.find_all('span', class_='infocard-lg-data text-muted')
        for i in range(len(id_list)):
            id_list[i] = id_list[i].find('small').text.rstrip("\n")
            id_list[i] = int ( ''.join(filter(str.isdigit, id_list[i]) ))
        return id_list

    def __get_name__(self, soup: bs) -> list:
        """Return pokemon name list
        Args:
            soup (bs): BeautifulSoup
        Returns:
            list: poke_list[str]
        """
        list_name = soup.find_all('a', class_='ent-name')
        poke_list = []
        for i in list_name:
            poke_list.append(i.text)
        return poke_list
    
    def __get_img__(self, soup: bs) -> list:
        """Return pokemon images list
        Args:
            soup (bs): BeautifulSoup
        Returns:
            list: img_list[str]
        """
        img_list = []
        poke_img_aux = []
        tag_img = soup.find_all('span',class_='infocard-lg-img')
        for i in tag_img:
            poke_img_aux.append(i.find_all('span', class_='img-fixed img-sprite'))
        for i in range(len(poke_img_aux)):
            img_list.append(poke_img_aux[i][0]['data-src'])
        return img_list

    def __get_type1__(self, soup: bs) -> list:
        """Return pokemon type 1 list
        Args:
            soup (bs): BeautifulSoup
        Returns:
            list: type1_list[str]
        """
        poke_type = []
        poke_card = soup.find_all('span', class_='infocard-lg-data text-muted')
        for i in poke_card:
            poke_type.append(i.find_all('a', class_='itype'))
        type1_list = []
        for i in range(len(poke_type)):
            type1_list.append(poke_type[i][0]['href'][6:])
        return type1_list

    def __get_type2__(self, soup: bs) -> list:
        """Return pokemon type 2 list
        Args:
            soup (bs): BeautifulSoup
        Returns:
            list: type2_list[str]
        """
        poke_type = []
        poke_card = soup.find_all('span', class_='infocard-lg-data text-muted')
        type2_list = []
        for i in poke_card:
            poke_type.append(i.find_all('a', class_='itype'))
        for i in poke_type:
            if len(i) > 1:
                type2_list.append(i[1]['href'][6:])
            else:
                type2_list.append('')
        return type2_list

    def __get_card_url__(self, soup: bs) -> list:
        """Return urls list
        Args:
            soup (bs): BeautifulSoup
        Returns:
            list: url[str]
        """
        url = []
        list_pokemon = self.__get_name__(soup)

        for i in list_pokemon[:150]:
            urlaux = 'https://www.pokemon.com/br/pokedex/' + str(i)
            url.append(urlaux)
        return url
    
    def __get_card_info__(self, soup:bs) -> list:
        """Return pokemon description list
        Args:
            soup (bs): BeautifulSoup
        Returns:
            list: description[str]
        """
        description = []
        url = self.__get_card_url__(soup)

        for i in url: 
            r = requests.get(i)
            if r.ok:
                soup = bs(r.text, 'lxml')
                descriptionaux = soup.find('p', class_='version-x active').text.strip()
                description.append(descriptionaux)
            else:
                description.append('')
        return description

    def __get_card_height__(self, soup:bs) -> list:
        """Return pokemon height list
        Args:
            soup (bs): BeautifulSoup
        Returns:
            list: height[float]
        """
        height = []
        url = self.__get_card_url__(soup)

        for i in url: 
            r = requests.get(i)
            if r.ok:
                soup = bs(r.text, 'lxml')
                heightaux = soup.find_all('span', class_='attribute-value')[0]
                height.append(heightaux.text)
            else:
                height.append('')
        for i in range(len(height)):
            if (height[i] != ''):
                height[i] = height[i].strip(" m")
                height[i] = round(float(height[i]),1)
        return height

    def __get_card_weight__(self, soup:bs) -> list:
        """Return pokemon weight list
        Args:
            soup (bs): BeautifulSoup
        Returns:
            list: weight[float]
        """
        weight = []
        url = self.__get_card_url__(soup)

        for i in url: 
            r = requests.get(i)
            if r.ok:
                soup = bs(r.text, 'lxml')
                weightaux = soup.find_all('span', class_='attribute-value')[1]
                weight.append(weightaux.text)
            else:
                weight.append('')
            for i in range(len(weight)):
                if (weight[i] != ''):
                    weight[i] = weight[i].strip(" kg")
        return weight

    def __get_card_ability__(self, soup:bs) -> list:
        """Return pokemon abilities list
        Args:
            soup (bs): BeautifulSoup
        Returns:
            list: ability[str]
        """
        ability = []
        url = self.__get_card_url__(soup)

        for i in url: 
            r = requests.get(i)
            if r.ok:
                soup = bs(r.text, 'lxml')
                abilitiesaux = soup.find_all('span', class_='attribute-value')[4]
                ability.append(abilitiesaux.text)
            else:
                ability.append('')
        return ability

    def _build_json(self, soup: bs) -> pd.DataFrame:
        """built dataframe of pokemon's stats ['id','pokemon','type_1','type_2','height_m','weight_kg','description','ability',''img_url]
        Args:
            soup (bs): BeautifulSoup
        Returns:
            pd.DataFrame: df_pokemon_stats
        """
        df = pd.DataFrame(
            columns=[
                'id', 
                'pokemon',
                'type_1', 
                'type_2', 
                'height_m', 
                'weight_kg', 
                'description', 
                'ability' , 
                'img_url'
            ]
        )

        list_id = self.__get_id__(soup)
        list_pokemon = self.__get_name__(soup)
        list_type1 = self.__get_type1__(soup)
        list_type2 = self.__get_type2__(soup)
        list_height = self.__get_card_height__(soup)
        list_weight = self.__get_card_weight__(soup)
        list_description = self.__get_card_info__(soup)
        list_ability = self.__get_card_ability__(soup)
        list_image = self.__get_img__(soup)

        for i in range(len(list_id[:150])):
            df2 = pd.DataFrame(
                {
                    'id' : [list_id[i]],
                    'pokemon' :[list_pokemon[i]],
                    'type_1' : [list_type1[i]], 
                    'type_2' : [list_type2[i]],
                    'height_m' :[list_height[i]],
                    'weight_kg' :[list_weight[i]],
                    'description' : [list_description[i]],
                    'ability' :[list_ability[i]],
                    'img_url' : [list_image[i]],

                }
            )
            df = pd.concat([df, df2], ignore_index=True)
        return df

    def scrapping_pokemon(self) -> pd.DataFrame:
        """Return dataframe to be consumed in main program
        Returns:
            pd.DataFrame: dataframe with pokemon stats
        """
        r = requests.get(self.url)
        soup = bs(r.text, "lxml")
        return self._build_json(soup)

    


