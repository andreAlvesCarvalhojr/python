cache_users = {}

def obter_usuario(user_id: int):
    if user_id in cache_users:
        print(f"Cache hit for user_id {user_id}")
        return cache_users[user_id]
    
    print(f"Cache miss for user_id {user_id}")

    # Simula a obtencao do usuario de uma fonte externa (banco de dados, API, etc.)
    usuario = {
        "id": user_id,
        "nome": f"Usuario {user_id}",
        "email": f"usuario{user_id}@example.com"
    }
    cache_users[user_id] = usuario
    return usuario

user1 = obter_usuario(123) #cache miss
user2 = obter_usuario(223) #cache Hit
user3 = obter_usuario(1423) #cache miss

print(f"\nTotal em cache: {len(cache_users)}")
print(f"IDs em cache: {list(cache_users.keys())}")