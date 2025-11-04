import os

# =======Tipos de Dados e Anotações de Tipo em Python

#Texto
texto_simples:str = 'Qualquer coisa'
texto_bytes:bytes = b'Qualquer coisa'

#Numeros
inteirinho:int = 42
flutuante:float = 10.5

#Booleano
verdadeiro:bool = True
falso:bool = False

#Coleções
lista:list = ['Meu nome', 24, False, None, b'ByteString']
tupla: tuple = ('abc', 12)
lista_set:set = ('abc', 123, 45.6)
dicionario:dict = {'chave1': 'valor1', 2:3}

#tupla[0] = 'def'  # Isso gera um erro, pois tuplas são imutáveis

variavel:any = None
variavel = lista

os.system("clear")
print(f'O valor da variavel e: {variavel}')
print(f'Tipo da variavel e: {type(variavel)}')

# =======Condicionais e Laços de Repetição

valor1:bool = True
valor2:None = None
valor3:int = 0


#Limpando o terminal
os.system("clear")

booleano: bool = False

if not texto_bytes: 
    print('Verdadeiro')
else:
    print('Falso')


num1: int = 1
num2: int = num1

if num1 is num2:
    print('Verdadeiro')
else:
    print('Falso')


user_input: str = input('Digite a sua operação: \n\n[0]:Adição\n[1]:Subtração\n[2]:Multiplicação\n[3]:Divisão\n\n')

match user_input:
    case "0": print('Somando')
    case "1": print('Subtraindo')
    case "2": print('Multiplicando')
    case "3": print('Dividindo')
    case _: print('Operação inválida')  # Caso padrão

for i in range(3, 10):
    print(i+1)

valor_inicial: int = int(input('Digite o valor inicial:\n'))
valor_final: int = int(input('Digite o valor final:\n'))

for i in range(valor_inicial, valor_final+1):
    print(i)

for i, nome in enumerate(['Ana', 'Bruno', 'Carlos']):
    print(f'{i} - {nome}')
    

cont: int = 0
target:int = 1000

while cont <= target:
    print(cont)
    cont += 1