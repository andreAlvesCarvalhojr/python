from enum import Enum
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"sistema": "NOt_Monolith", "versao": "1.0"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item_type = str(type(item_id))
    return {"item_id": item_id, "item_type": item_type}

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{name}")
def get_model(name: ModelName):
    if name == ModelName.alexnet:
        return {"model_name": name, "message": "Deep Learning FTW!"}
    if name.value == "lenet":
        return {"model_name": name, "message": "LeCNN all the images"}
    return {"model_name": name, "message": "Have some residuals"}