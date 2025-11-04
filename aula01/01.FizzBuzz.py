from re import findall


def FizzBuzz(limite:int) -> None:
    string = 'FizzBuzz'

    palavras = findall(r'[A-Z][a-z]*', string)

    for n in range (1, limite+1):
        if n % 3 == 0 and n % 5 == 0:
            print(f'{n}: {palavras[0]}')
        elif n % 3 == 0:
            print(f'{n}: {palavras[1]}')
        elif n % 5 == 0:
            print(f'{n}: {palavras[2]}')
        else:
            print(n)    

if __name__ == "__main__":
    FizzBuzz(100)