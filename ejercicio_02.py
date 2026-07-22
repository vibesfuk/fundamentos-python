class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.__titulo = titulo
        self.__artista = artista
        self.__duracion = duracion

    def get_titulo(self):
        return self.__titulo
    def get_artista(self):
        return self.__artista
    def get_duracion(self):
        return self.__duracion
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_artista(self, artista):
        self.__artista = artista

    def set_duracion(self, duracion):
        self.__duracion = duracion


Cancion = Cancion("xxxtentacion","Fuck Love","2:26")
print("Título:", Cancion.get_titulo())
print("Artista:", Cancion.get_artista())
print("Duración:", Cancion.get_duracion())

Cancion.set_duracion("2:00")
print("\nDespués de actualizar la duración:")
print("Duración:", Cancion.get_duracion())