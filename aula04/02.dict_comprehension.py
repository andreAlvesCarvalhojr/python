lista_nome:list = ['João', 'Maria', 'Roberto', 'Ana', 'Gustavo', 'Patrícia', 'Carla', 'Pedro', 'Andre']

teste:str = lista_nome[0]
teste_letter:str = teste[-1]

print(teste)
print(teste_letter)

dict_sexo:dict = {
    nome: 'Masculino' if nome.endswith('o') else 'Feminino' for nome in lista_nome
}

print(dict_sexo)

print([n for n in range(1,int(input('Digite um número:\n> ')) + 1) if n % 2 == 0 ] )