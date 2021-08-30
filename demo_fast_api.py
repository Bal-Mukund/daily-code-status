#uvicorn fileName:app --reload

from fastapi import  FastAPI , Path
from  typing import  Optional
from pydantic import BaseModel

app = FastAPI()

class value(BaseModel):
    name :     str
    price : Optional[float] = None
    brand : Optional[str] = None

class update_value(BaseModel):
    name : Optional[str] = None
    price : Optional[float] = None
    brand : Optional[str] = None

stock = {}

@app.get("/")
def home():
    return "welcome home"



@app.get("/find-by-id/{id}")
def find_by_id(id: str = Path(None,description="enter key here to find values")):
    if id not in stock.keys():
        return "not in stock"

    return stock[id]


@app.get("/find-by-name")
def find_by_name(name: str):
    for id in stock:
        if stock[id].name == name:
            return stock[id]

    return  "not in stock"


@app.post("/add-in-stock/{id}")
def add_in_stock(id: str ,value : value):
    stock[id] = value
    return f"{value.name}  added in stock"


@app.put("/update-stock/{id}")
def update_stock(id: str,update_value: update_value):
    if update_value.name != None:
        stock[id].name  = update_value.name

    if update_value.price != None:
        stock[id].price  = update_value.price

    if update_value.brand != None:
        stock[id].brand  = update_value.brand

    return  f"{id} updated"


@app.delete("/remove-from-stock/{id}")
def remove_from_stock(id: str = Path(None, description= "id of item you want to remove")):
   if id in stock.keys():
        del stock[id]
        return f"{id} removed from stock"

   return f"{id} already out of stock"