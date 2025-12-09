from test_module.main import calcular_dobro

def test_calcular_dobro():
    resposta = calcular_dobro(5)
    assert resposta == 10