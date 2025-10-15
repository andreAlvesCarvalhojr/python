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


tecnoloigias = {"Python", "Java", "JavaScript"}
print(tecnoloigias)

#Operacoes de conjutos
backend_devs = {"Ana", "Bruno", "Carlos"}
frontend_devs = {"Daniel", "Bruno", "Eduardo"}

#Interseção (quem faz ambos?)
fullstack = backend_devs & frontend_devs # Bruno

#União (todos os devs)
todos_devs = backend_devs | frontend_devs

#Diferença (quem faz backend mas nao faz frontend?)
so_backend = backend_devs - frontend_devs # Ana, Carlos
