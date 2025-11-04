import meu_modulo

global CONTADOR

def increment(num:int) -> None:
    CONTADOR = 0
    cont = CONTADOR
    for i in range(num+1):
        cont += 1
    print (cont)

if __name__ == "__main__":
    increment(10000)


def argumentos(**args) -> dict:
    '''Éssa função retorna um dicionário com os argumentos nomeados passados para ela.'''
    return args

if __name__ == "__main__":
    args = argumentos(nome="Ana", idade=30, cidade="São Paulo")
    print(type(args))
    print(args)

    
if __name__ == "__main__":
    numero = 7
    resultado = meu_modulo.valor_tipo(numero)
    print(f'O número {numero} é {resultado}.')
    print(type(resultado))