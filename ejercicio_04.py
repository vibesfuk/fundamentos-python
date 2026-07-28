from fastapi import FastAPI
from pydantic import BaseModel
from fastapi. middleware.cors import CORSMiddleware

class Categoria(BaseModel):
    id: int
    marca: str
    modelo: str 
app = FastAPI()

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "hello world"}

@app.get ("/celulares")
async def obtenerCelulares():
    return [
        {"id": 1, "marca": "Apple", "modelo": "iPhone 15 Pro"},
        {"id": 2, "marca": "Samsung", "modelo": "Galaxy S24 Ultra"},
        {"id": 3, "marca": "Xiaomi",  "modelo": "Redmi Note 13"},
    ] 

