#=====lista

#lista mutavel
lista = []

#tupla imutavel
tupla = ()

#lista mutavel
usuario = ["Ana", "Maria", "Pedro"]
#atualiza o valor de um elemento
usuario.append("Daniel")
#insere em uma posicao especifica
usuario.insert(1, "Carla")
#remove o ultimo elemento da lista
usuario.remove("Pedro")
#remove o  elemento da posicao especifica
ultimo = usuario.pop()
#retorna o indice do elemento
usuario[usuario.index("Ana")] = "Ana Clara"
print(usuario)
print(ultimo)



#tupla imutavel
coordenadas = (10.0, 20.0)

def obter_usuario():
    return ("Eduardo", 30, "Masculino")

nome, idade, genero = obter_usuario()
print(nome, idade, genero)