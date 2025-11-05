class Carro:

    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def __repr__(self):
        return f"Carro(marca='{self.marca}', modelo='{self.modelo}', ano={self.ano}, preco={self.preco})"
    
    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.ano}) - R$ {self.preco:,.2f}'
    
    def __eq__(self, other):
        if isinstance(other, Carro):
            carro_1 = (self.marca, self.modelo)
            carro_2 = (other.marca, other.modelo)
            if carro_1 == carro_2: return True
        return False
    
    def __gt__(self, other):
        if not isinstance(other, Carro):
            return None
        preco_1 = self.preco
        preco_2 = other.preco
        if preco_1 > preco_2: return True
        return False

    def __lt__(self, other):
        if not isinstance(other, Carro):
            return None
        return self.preco < other.preco


class Concessionaria:

    def __init__(self, nome:str, positions:int, arquivo_carros:str = None, dicio_carros:dict = []):
        self.nome = nome
        self.arquivo_carros = arquivo_carros
        self.dicio_carros = dicio_carros

        self.empty_positions:list[int] = [range(1,positions+1)]
        self.complete_positions:list[int] = []


    def __repr__(self):
        return f"Concessionaria(nome='{self.nome}', positions={self.positions}, arquivo_carros='{self.arquivo_carros}', dicio_carros={self.dicio_carros})"

    def __str__(self):
        return f'Concessionária {self.nome} - Vagas: {self.positions} Posições '

    def __add__(self, other):
        if not isinstance(other, Carro):
            raise Exception('Só é possível adicionar objetos do tipo Carro')
        if other in self.dicio_carros.values():
            return False
        

        self.dicio_carros[self.empty_positions] = other
        self.complete_positions.append(self.empty_positions)
        self.empty_positions.pop(0)

    
    def __sub__(self, other):
        if not isinstance(other, Carro):
            raise Exception('Só é possível remover carros!')

        deletar = None
        for vaga, carro in self.dicio_carros.items():
            if carro == other:
                deletar = vaga
                break

        if deletar is not None:
            self.empty_positions.append(deletar)
            self.complete_positions.remove(deletar)
            del self.dicio_carros[deletar]
            return True

        return False
    
    def add_cars(self):
        from json import loads as json_loads
        with open(self.arquivo) as f:
            dicio_carros:dict = json_loads(f.read())
        for carro in dicio_carros.values():
            marca, modelo, ano, preco = carro
            car = Carro(marca, modelo, ano, preco)
            self + car
    


if __name__ == "__main__":

    lista_carros = []

    test_car = Concessionaria('Teste', 5)

    ka = Carro('Ford', 'Ka', 2020, 45000.00)
    mclaren = Carro('McLaren', 'F1-GTR', 1996, 15000000.00)
    charger = Carro('Dodge', 'Charger SRT Hellcat', 2021, 350000.00)

    lista_carros.append(ka)
    lista_carros.append(mclaren)
    lista_carros.append(charger)

    #print(lista_carros)
