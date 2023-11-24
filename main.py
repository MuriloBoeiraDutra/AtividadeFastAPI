from fastapi import FastAPI
from typing import Optional, Text
from pydantic import BaseModel
import math

app = FastAPI()


@app.get("/quadrados/")
def quadrados(max:Optional[int] = 4):
    lista = []

    for contador in range(1,max+1):
        lista.append(contador*contador)

    return{
        "max":max,
        "quadrados":lista
    }

@app.get("/tabuada/")
def tabuada(numero: Optional[int] = 5, comeco: Optional[int] = 1, fim: Optional[int] = 10):
    lista = []

    for contador in range(comeco, fim+1):
        lista.append(contador*numero)

    return {
        "num":numero,
        "start":comeco,
        "end":fim,
        "tabuada":lista
    }

class FraseJson(BaseModel):
    escrita : str

@app.post("/frases/")
def frases(frase: FraseJson):
    frase.escrita
    vogal = 0
    outro = 0
    espaco = 0
    for letra in frase.escrita:
        if letra in "aeiouAEIOU": 
            vogal = vogal + 1
        elif letra == " ":
            espaco = espaco + 1
        else:
            outro = outro + 1
    return{
        "frase": frase.escrita,
        "vogais": vogal,
        "espaços": espaco,
        "outros": outro
    }

class Json(BaseModel):
    a : float
    b : float
    c : float

@app.post("/equacao/")
def equacao(equacao:Json):
    a, b, c = equacao.a, equacao.b, equacao.c

    equacao_txt = f"{a}x²{b:+}x{c:+}"
    delta = b**2-4*a*c
    variavel1 = (-b + math.sqrt(delta)) / (2*a)
    variavel2 = (-b - math.sqrt(delta)) / (2*a) 
    
    return{
        "eq": equacao_txt,
        "x1": variavel1,
        "x2": variavel2
    }
