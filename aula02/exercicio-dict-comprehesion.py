from collections import defaultdict

#Transforme uma lista de pedidos em um dicionário {cliente: total_gasto}, mas apenas para clientes com mais de R$ 100 em compras.
pedidos = [
    {"cliente": "Ana", "valor": 50.00},
    {"cliente": "Bruno", "valor": 150.00},
    {"cliente": "Ana", "valor": 80.00},  # Ana: 130 total
    {"cliente": "Carlos", "valor": 30.00},
    {"cliente": "Bruno", "valor": 50.00},  # Bruno: 200 total
]

# Desafio: Usar dict comprehension + sum()

totais = defaultdict(float)
for pedido in pedidos:
    totais[pedido["cliente"]] += pedido["valor"]

clientes_vip = {cliente: total for cliente, total in totais.items() if total > 100}
print(clientes_vip)  # {'Ana': 130.0, 'Bruno': 200.0}