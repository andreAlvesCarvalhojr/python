class User:
    name: str
    age: int
    email: str
    password: str
    address: str

    def __init__(self, name: str, age: int, email: str, password: str, address: str):
        self.name = name
        self.age = age
        self.email = email
        self.password = password
        self.address = address

    def __str__(self):
        return f"User(name={self.name}, age={self.age}, email={self.email}, address={self.address})"
    
    def __repr__(self):
        return f"User(name={self.name}, age={self.age}, email={self.email}, address={self.address})"
    

