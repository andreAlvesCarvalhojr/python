from pydantic import BaseModel, Field
from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/items/')
def get_item(store_id:int=0, barcode:str="12345678"):
    return {"store_id":store_id, "barcode":barcode}

@app.get('/search/')
def search_item(q:str = Query(..., max_length=10)):
    return q

class UserSchema(BaseModel):
    username:str
    email:str
    age:int = Field(gt=17)
    is_active:bool = True

@app.put('/users/{user_id}')
def put_user(user_id:int, user_data:UserSchema, wait_for_save:bool = False):
    return {
        "User ID (Enviado No Path)":user_id,
        "User Data (Enviado no Body)":user_data,
        "Wait For Save (Enviado na Query)":wait_for_save
    }