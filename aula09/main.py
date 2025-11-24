
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Lista para armazenar os jogos (simulando um banco de dados)
games_db = []

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Games!", "endpoints": {"/games/": "POST para criar, GET para listar", "/docs": "Documentação da API"}}

class Game(BaseModel):
    name:str
    price:float
    score:float
    plataform:list[str]

@app.get("/games/")
def list_games():
    return {"games": games_db, "total": len(games_db)}

@app.post("/games/")
def create_game(game:Game):
    # Adicionar o jogo à lista
    games_db.append(game.model_dump())
    return {"message": f"{game.name} criado com sucesso!", "game": game.model_dump(), "total_games": len(games_db)}




clientes_db = []

@app.get("/cliente/")
def list_clientes():
    return {"clientes": clientes_db, "total": len(clientes_db)}

class Cliente(BaseModel):
    name: str
    email: str
    id:int


@app.get("/cliente/{cliente_id}")
def get_cliente_info(cliente_id: int):
    # Buscar cliente pelo ID
    for cliente in clientes_db:
        if cliente["id"] == cliente_id:
            return cliente
    return {"error": "Cliente não encontrado"}

@app.post("/cliente/")
def create_cliente(cliente: Cliente):
    # Adicionar cliente à lista
    clientes_db.append(cliente.model_dump())
    return {"message": f"Cliente {cliente.name} criado com sucesso!", "cliente": cliente.model_dump(), "total_clientes": len(clientes_db)}
