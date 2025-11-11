import requests
from json import loads as json_loads

BASE_URL = "https://api.disneyapi.dev"

FETCH = "character"

query = f'{BASE_URL}/{FETCH}?name=MickeyMouse'
get_all = f'{BASE_URL}/{FETCH}'
get_by_id = f'{BASE_URL}/{FETCH}/308'

def fetch_json(url: str) -> dict:
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return json_loads(resposta.text)
        else:
            print(f'Error fetching {url}: Status Code {resposta.status_code}')
            return {}
    except requests.RequestException as e:
        print(f'Error fetching {url}: {e}')
        return {}


all_characters = fetch_json(get_all)
character_by_id = fetch_json(get_by_id)

all_chars = requests.get(query).content
response_data = json_loads(all_chars)
meus_chars = response_data.get('data', [])

# Verificar se temos pelo menos 2 caracteres
if len(meus_chars) >= 2:
    char_1, char_2 = meus_chars[0], meus_chars[1]
elif len(meus_chars) == 1:
    char_1 = meus_chars[0]
    char_2 = None
    #print("Apenas 1 personagem encontrado")
else:
    #print("Nenhum personagem encontrado na busca específica")
    # Usar dados da busca geral como fallback
    data = fetch_json(get_all)['data']
    if len(data) >= 2:
        char_1, char_2 = data[0], data[1]
        #print("Usando os primeiros 2 personagens da lista geral")
    else:
        char_1 = char_2 = None
        #print("Não foi possível obter personagens")

#print(character_by_id)

# if char_1:
#     print(f"Personagem 1: {char_1.get('name', 'Nome não disponível')}")
# if char_2:
#     print(f"Personagem 2: {char_2.get('name', 'Nome não disponível')}")
# else:
#     print("Segundo personagem não disponível")


class Disney:
    
    def __init__(self, id:int):
        self.id:int = id
        info = self.chamar_personagem()
        self.url:str = info.get('url')
        self.name:str = info.get('name')
        self.image_url:str = info.get('imageUrl')
        self.films:list[str] = info.get('films')
        self.short_films:list[str] = info.get('shortFilms')
        self.tv_shows:list[str] = info.get('tvShows')
        self.video_games:list[str] = info.get('videoGames')
        self.park_attractions:list[str] = info.get('parkAttractions')
        self.allies:list[str] = info.get('allies')
        self.enemies:list[str] = info.get('enemies')
    
    # def chamar_personagem(self) -> dict:
    #     url = f'{BASE_URL}/{FETCH}/{self.id}'
    #     info = fetch_json(url)
    #     if not info:
    #         return {}
    #     return info.get('data', {})
    
    def chamar_personagem(self) -> dict:
        response:requests = requests.get(f'{BASE_URL}/{FETCH}/{self.id}')
        raw_content:bytes = response.content
        parsed_content:dict = json_loads(raw_content)['data']
        return dict(parsed_content)
    
if __name__ == '__main__':
    personagem = Disney(308)
    # print(f'Nome: {personagem.name}')
    # print(f'Filmes: {personagem.films}')
    # print(f'TV Shows: {personagem.tv_shows}')
    # print(f'Inimigos: {personagem.enemies}')


    try:
        '''
        Nome: {nome}
        Imagem: {imageUrl}
        Filmes:
            {film1}
            {film2}
            {film3}
        Video Games:
            {vg1}
            {vg2}
        '''
        id = '4703'
        char = Disney(id)
        #first_name = char.name.split(' ')[0]
        print(f'Nome: {char.name}')
        print(f'Imagem: {char.image_url}')
        print('Filmes:')
        for filme in char.films:
            print('\t-',filme)
        print('Video Games:')
        for vg in char.video_games:
            print('\t-',vg)
    except KeyboardInterrupt:
        exit()