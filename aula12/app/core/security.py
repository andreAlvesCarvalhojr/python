from passlib.context import CryptContext

contexto_senha = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password(password: str) -> str:
    return contexto_senha.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return contexto_senha.verify(plain_password, hashed_password)


if __name__ == "__main__":
    print('Testing.....')
    print('[!] Warning: This should not be used in production!\n')

    senha = input("Digite a senha a ser criptografada: \n")
    hashed = get_password(senha)

    is_password = verify_password(senha, hashed)
    print(f"Senha criptografada: {hashed}")
    print(f"Senha verificada: {is_password}")