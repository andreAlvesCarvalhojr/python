# ========== Exercício 01 ==========

lista_nomes:list = ['ana', 'bruno', 'carla', 'daniel', 'elaine', 'fabio']

dict_UpperCase:dict = {
    nome.upper() for nome in lista_nomes
}

print(dict_UpperCase)

dict_CammelCase:dict = {
    nome.title() for nome in lista_nomes
}

print(dict_CammelCase)


# ========== Exercício 02 ==========

lista_numeros:list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista:list = [
    n for n in lista_numeros if n >= 8
]

print(lista)
