from lista_enlazada import  DoubleLinkedList
class Cancion :

    def __init__(self, titulo: str, artista: str, duracion: int):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
        
        
    def __repr__(self):
        return f"{self.titulo} -- {self.artista} -- {self.duracion}s"
