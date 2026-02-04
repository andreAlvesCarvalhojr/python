from curses import wrapper


def log_ativo(funcao):
    def wrapper(*args, **kwargs):
        print(f"Executando a função: {funcao.__name__}")
        funcao(*args, **kwargs)
        print(f"Função {funcao.__name__} executada com sucesso.")
        return wrapper
    

def cronometro(funcao):
    import time

    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução da função {funcao.__name__}: {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

@cronometro
def processar_dados():
    import time as sleep
    print("Processando dados...")
    sleep.sleep(2)  # Simula uma operação demorada
    print("Dados processados com sucesso!")

import logging
processar_dados()