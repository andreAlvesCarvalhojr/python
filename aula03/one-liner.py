def checkar_par_antigo(num: int) -> bool:
    '''Função que verifica se um número é par (versão antiga).'''
    if num % 2 == 0:
        return True
    else:
        return False
    
def checkar_par(num: int) -> bool:
    '''Função que verifica se um número é par (versão one-liner).'''
    return 'par' if num % 2 == 0 else 'ímpar'

if __name__ == "__main__":
    numero = int(input("Digite um número inteiro: "))
    print(f'O número {numero} é {checkar_par_antigo(numero)} (antigo).')
    print(f'O número {numero} é {checkar_par(numero)} (one-liner).')