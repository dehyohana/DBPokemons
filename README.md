# DBPokemons
Repositório de códigos criados para extrair e consolidar informações dos pokemons através de páginas web, criar uma tabela com os valores e salvar em banco de dados MySQL.

Páginas consultadas:
- https://pokemondb.net/pokedex/national
- https://www.pokemon.com/br/pokedex

## Tech
Tecnologias empregadas:

- [Python] - Linguagem de programação de alto nível e de propósito geral. 
- [MySQL] - Sistema de gerenciamento de banco de dados.
- [Virtualenv] -  Permite a execução do projeto em um ambiente virtual, isto é, ela empacota todas as dependências que um projeto precisa e armazena em um diretório, fazendo com que nenhum pacote seja instalado diretamente no sistema operacional


## Installation
Primeiro, instale o pip:

```sh
sudo apt-get install python3-pip
```


Instale o virtual env utilizando o pip:
```sh
sudo pip3 install virtualenv
```

## Utilização
Clone o repositório:

```sh
git clone https://github.com/dehyohana/DBPokemons.git
```

Após instalar os recursos e clonar o projeto, caso deseje criar um ambiente virtual de execução com as bibliotecas necessárias para a execução, utilize o seguinte comando no diretório do projeto:

```sh
make init
```

Ative o ambiente virtual através do comando:

```sh
source .venv/bin/activate
```

Crie variáveis ambientes com as credenciais para conexão do banco de dados. Por exemplo, posso criar um arquivo .env com as seguintes variáveis ambientes:

```sh
 POSTGRES_USER=root
 POSTGRES_PASSWORD=root
 POSTGRES_DATABASE=pokedex
 POSTGRES_ADDRESS=localhost
 ``` 

 Atenção, o banco de dados (neste caso, pokedex) já deve ter sido criado no mysql.

Após ativar o ambiente virtual, rode o programa main. O programa irá iniciar e ao final deve criar uma tabela "pokemon" no banco de dados. 

[Python]: https://www.python.org/
[MySQL]:https://www.mysql.com/
[Virtualenv]: https://gist.github.com/frfahim/73c0fad6350332cef7a653bcd762f08d