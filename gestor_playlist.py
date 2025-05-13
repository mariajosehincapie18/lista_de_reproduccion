from lista_enlazada import DoubleLinkedList
from cancion import Cancion

class Gestor_paylist():
    def __init__(self):
        self.playlist= DoubleLinkedList()

    def agregar_cancion_a_playlist(self, titulo:str, artista:str, duracion:int):
        actual = self.playlist._DoubleLinkedList__head
        for _ in range(self.playlist._DoubleLinkedList__size):
            if actual.value.titulo == titulo:
                print(f"No es posible agregar la cancion {titulo} ya existe")
                return
            if duracion < 10 or duracion > 15:
                print("no es posible agregar a la playlist tiempo excedido")
                return
            actual = actual.next

        nueva_cancion= Cancion(titulo, artista, duracion)
        self.playlist.append(nueva_cancion)
        print(f" Cancion {titulo} , artista: {artista}, { duracion}s fue agregada con exito")



gestor= Gestor_paylist()
gestor.agregar_cancion_a_playlist("s91", "karol g", 10)
gestor.agregar_cancion_a_playlist("milagros", "karol g", 15 )
gestor.agregar_cancion_a_playlist("romantico de lunes", " feid", 11 )
gestor.agregar_cancion_a_playlist("dia tras dia", " andres cepeda", 10 )
gestor.agregar_cancion_a_playlist("admv", " maluma", 13 )
print(gestor.playlist)

head= gestor.playlist._DoubleLinkedList__head
tail = gestor.playlist._DoubleLinkedList__tail
print(head.prev)
print(tail.next)



    


  