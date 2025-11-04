import os
from typing import Self

# =======Desafio 1

# class User():
#     def __init__(self, id: str, nome: str, email: str, ativo: bool, tags: list[str]):
#         self.id = id
#         self.nome = nome
#         self.email = email
#         self.ativo = ativo
#         self.tags = tags

        
# def main():
#     user = User("1", "John Doe", "", True, ["admin", "user"])
#     print(f"ID: {user.id}")
#     print(f"Nome: {user.nome}")
#     print(f"Email: {user.email}")
#     print(f"Ativo: {user.ativo}")
#     print(f"Tags: {user.tags}")

# if __name__ == "__main__":
#     main()



# =========Desafio 2

# tempos_resposta  = [50, 120,450,1200, 80, 950]

# for tempo in tempos_resposta:
#     if tempo <= 100:
#         print(f"Tempo de resposta {tempo}ms: Excelente")
#     elif tempo in range(100, 300):
#         print(f"Tempo de resposta {tempo}ms: Bom")
#     elif tempo in range(300, 1000):
#         print(f"Tempo de resposta {tempo}ms: Aceitavel")
#     elif tempo > 1000:
#         print(f"Tempo de resposta {tempo}ms: Lento")



# class Pessoa:
#     def __init__(self, nome: str, idade: int, cpf: str):
#         self.nome = nome
#         self.idade = idade
#         self.cpf = cpf # Atributo privado 
#         # self.__cpf = cpf # Atributo fortemente privado

#     @property
#     def cpf(self) -> str:
#         return self._cpf
    
#     @cpf.setter
#     def cpf(self, valor: str) -> None:
#         if len(valor) == 11 and valor.isdigit():
#             self._cpf = valor
#         else:
#             raise ValueError("CPF deve conter 11 dígitos numéricos.")   

#     def apresentar(self) -> str:
#         return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
#     def __str__(self) -> str:
#         return f"Nome: {self.nome}, Idade: {self.idade}"

#     def __repr__(self) -> str:
#         return f"Pessoa(nome={self.nome!r}, idade={self.idade!r})"

# if __name__ == "__main__":
#     pessoa = Pessoa("João", 30, "12345678901")
#     print(pessoa.apresentar())
#     # pessoa.cpf = "109876543"
#     # print(pessoa)



