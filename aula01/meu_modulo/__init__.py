print("Hello from meu_modulo!")

def valor_tipo(numero: int) -> type:
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"