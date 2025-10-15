quadrados = {x: x**2 for x in range(5)}

#Mesclando dicionarios (Python 3.9+)
config_default = { "timeout": 30, "retries": 3}
config_usuario = { "timeout": 60}
config_final = config_default | config_usuario
print(config_final)

api_response = {
    "status": "success",
    "data": [
        {"id": 1, "nome": "Ana", "email": "ana@example.com"},
        {"id": 2, "nome": "Bruno", "email": "bruno@example.com"},
        {"id": 3, "nome": "Carlos", "email": "carlos@example.com"}
    ],
    "meta": {"page": 1, "per_page": 10, "total": 3}
}

#acesso seguro a dados aninhados
primeiro_usuario = api_response.get(
    "data", {}
).get("usuario", {})
print(primeiro_usuario)