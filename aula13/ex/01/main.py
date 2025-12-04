from http.client import HTTPException
from fastapi import FastAPI, status, HTPPException, Response

app = FastAPI()

@app.patch("/users/{uid}", status_code=status.HTTP_200_OK)
def update_user(uid: int):
    return {"uid": uid, "message": "User updated successfully"}

@app.delete("/users/{uid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(uid: int):
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/users/{uid}", status_code=status.HTTP_200_OK)
def get_user(uid: int):
    if uid != 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"uid": uid, "name": "John Doe"}

@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(name: str):
    return {"uid": 1, "name": name}