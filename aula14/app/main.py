from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": 200, "message": "O app está funcionando corretamente! "}

@app.get("/health")
def health():
    return {"status": 200}

@app.get("/users/me")
def read_user_me():
    return {"user_id": "the current user"}