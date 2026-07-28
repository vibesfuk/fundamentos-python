from fastapi import FastAPI
from fastapi. middleware.cors import CORSMiddleware
from pydantic import BaseModel

class IniciarCancion(BaseModel):
    cancion: str 

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
    return {"massage": "hello world"}

@app.get("/ejercicio/{campo}")
async def obtenerCampo(campo):
    return {"campo": campo}  

@app.get("/libros") 
async def obtenerLibros():
    return [
        {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
        {"id": 2, "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes"},
        {"id": 3, "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry"},
