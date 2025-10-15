# Logs de requisições (cada tupla e imutavel)
from typing import Counter


logs = [
    ("2024-06-10 10:00:00", "GET", "Application started", 200),
    ("2024-06-10 10:05:00", "POST", "An error occurred", 301),
    ("2024-06-10 10:10:00", "DELETE", "Application stopped", 204),
    ("2024-06-10 10:15:00", "GET", "Resource not found", 500),
]

erros = [log for log in logs if log[3] >= 400]

metodo = [log[1] for log in logs]
#print(f"Get: {metodo.count('GET')}")
#print(f"Post: {metodo.count('POST')}")

ultimos_logs = logs[2:]
#print(ultimos_logs)

logs_ordenados = sorted(logs, key = lambda x: x[3], reverse=True)
#print(f"Total de erros: {len(erros)}")
#print(f"Primeiro erro: {erros[0]}")

#=====Desafio 1

pedidos = [
    (1, "Ana", 150.00, "pago"),
    (2, "Bruno", 200.00, "pendente"),
    (3, "Ana", 100.00, "pago"),
    (4, "Carlos", 300.00, "pendente"),
    (5, "Ana", 50.00, "cancelado"),
]

pendentes = len([pedido for pedido in pedidos if pedido[3] == 'pendente'])
print(f"Pedidos pendentes: {pendentes}")

total_faturado = sum(pedido[2] for pedido in pedidos if pedido[3] != 'cancelado')
print(f"Total faturado: {total_faturado}")

#=Errado
clientes = [pedidos[1] for pedido in pedidos if pedido[3] != 'cancelado']
#top_cliente = Counter(clientes).most_common(1)[0][0]
print(f"Maior pedido: {clientes}")


#====Dicionario
usuario = {
    "id": 1234,
    "nome": "Ana",
    "email": "ana@example.com",
    "ativo": True,
}

user = usuario.get("telefone", "Telefone nao cadastrado")

for chave in usuario:
    print(f"{chave}: {usuario[chave]}")

for chave, valor in usuario.items():
    print(f"{chave}: {valor}")

for valor in usuario.vakues():
    print(valor)


if "email" in usuario.values():
    print("Email cadastrado")

if "email" in usuario:
    print("Email cadastrado")


