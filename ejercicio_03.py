from fastapi import FastAPI

app = FastAPI()

@app.get("/") 
async def root():
    return {"massage": "hello world"}

@app.get("/libros") 
async def obtenerLibros():
    return [
        {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
        {"id": 2, "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes"},
        {"id": 3, "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry"}
    ]