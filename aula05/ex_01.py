def calcular_media(numeros:list[int]) -> float:
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)