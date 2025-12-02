from hashlib import md5

class MockDB:
    banco_senha = {
        'admin': "21232f297a57a5a743894a0e4a801fc3",  # senha: admin
    }

user = input("Digite o nome de usuário: \n")
password = input("Digite a senha: \n")

encoded_pass = password.encode('utf-8')
md5_pass = md5(encoded_pass).hexdigest()

if user in MockDB.banco_senha and MockDB.banco_senha[user] == md5_pass:
    print("Acesso concedido!")
else:
    print("Acesso negado!")