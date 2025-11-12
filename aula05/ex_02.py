def classificar_imc(
        peso:float,
        altura:float
        ) -> str:
    num_imc = peso / (altura * altura)

    if num_imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= num_imc < 24.9:
        return 'Peso normal'
    elif 25.0 <= num_imc < 29.9:
        return 'Sobrepeso'
    elif 30.0 <= num_imc < 34.9:
        return 'Obesidade grau I'
    elif 35.0 <= num_imc < 39.9:
        return 'Obesidade grau II'
    else:
        return 'Obesidade grau III'
    
if __name__ == '__main__':
    peso_usuario:float = float(input('Digite seu peso (kg):\n> '))
    altura_usuario:float = float(input('Digite sua altura (m):\n> '))
    classificacao:str = classificar_imc(peso_usuario, altura_usuario)
    print(f'Sua classificação de IMC é: {classificacao}')