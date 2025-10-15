# Logs de requisições (cada tupla e imutavel)
logs = [
    ("2024-06-10 10:00:00", "GET", "Application started", 200),
    ("2024-06-10 10:05:00", "POST", "An error occurred", 301),
    ("2024-06-10 10:10:00", "DELETE", "Application stopped", 204),
    ("2024-06-10 10:15:00", "GET", "Resource not found", 500),
]

erros = [log for log in logs if log[3] >= 400]

metodo = [log[1] for log in logs]
print(f"Get: {metodo.count('GET')}")
print(f"Post: {metodo.count('POST')}")

ultimos_logs = logs[2:]
print(ultimos_logs)

logs_ordenados = sorted(logs, key = lambda x: x[3], reverse=True)
print(f"Total de erros: {len(erros)}")
print(f"Primeiro erro: {erros[0]}")