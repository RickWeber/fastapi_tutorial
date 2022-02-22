from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class BaseUrls(str, Enum):
    rick = "rick"
    other = "other"
    about = "about"

app = FastAPI()

@app.get("/{special}/")
async def get_special_page(special: BaseUrls):
    if special == BaseUrls.about:
        return {"about me": "NULL"}
    if special == BaseUrls.other:
        return {"data": "other"}
    if special == BaseUrls.rick:
        return {"who": "Rick", "url": "hirerick.com"}

@app.get("/models/{model_name}/")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}



"""
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/names/{item_name}")
async def read_item(item_name: str):
    return {"item_name": item_name}
"""