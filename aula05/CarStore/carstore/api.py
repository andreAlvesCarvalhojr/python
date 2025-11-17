from requests import get

URL = ''

def connect(veiculo:str, marca:str = None, modelo:str = None) -> dict:
    url = f'{URL}/{veiculo}/marcas/36/modelos'
    response = get(url)
    if response.status_code != 200:
        return {}
    return response.json()