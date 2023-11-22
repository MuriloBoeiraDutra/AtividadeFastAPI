from fastapi import FastAPI
from typing import Optional
import math

app = FastAPI()


@app.get("/quadrados/")
def quadrados(max:Optional[int] = 4):
    lista = []
    i = 0
    for i in range(1,max+1,i+1):
        lista.append(i*i)
    return{
        "max":max,
        "quadrados":lista
    }