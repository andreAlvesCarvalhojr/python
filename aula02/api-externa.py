#Dados de usuarios de uma API externa

usuario_api = [
    {"id": 1, "nome": "Ana", "idade": 28, "ativo": True},
    {"id": 2, "nome": "Bruno", "idade": 35, "ativo": False},
    {"id": 3, "nome": "Carla",  "idade": 22, "ativo": True},
    {"id": 4, "nome": "Daniel", "idade": 30, "ativo": True},
    {"id": 5, "nome": "Eduardo", "idade": 40, "ativo": False},
]

# 1- Filtrar usuarios ativos 
nomes_ativos = [user["nome"] for user in usuario_api if user["ativo"]]
print("Nomes ativos:", nomes_ativos)

# 2- Dicionario de Id e nome
id_para_nome = {user["id"]: user["nome"] for user in usuario_api}
print("ID para Nome:", id_para_nome)

# 3- Categorizar por faixa etaria
def categorizar_idade(idade):
    if idade < 30:
        return "Jovem"
    elif 30 <= idade < 40:
        return "Adulto"
    else:
        return "Sênior"

    categorias = {user["nome"]: categorizar_idade(user["idade"]) for user in usuario_api}
    print("Categorias por idade:", categorias)


# 4- Nested comprehension: Matriz de multiplicação

tabuada = [[i * j for j in range(1, 11)] for i in range(1, 11)]
print(tabuada[4][4])  # 5x5 = 25

# ❌ Complexo demais - prefira um for normal
resultado = [x for x in [y for y in [z for z in range(100) if z % 2 == 0] if y > 10] if x < 50]

# ✅ Melhor:
numeros = range(100)
pares = [n for n in numeros if n % 2 == 0]
filtrados = [n for n in pares if 10 < n < 50]