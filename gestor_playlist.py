from lista_enlazada import DoubleLinkedList
from cancion import Cancion
import time

class Gestor_paylist():
    def __init__(self):
        self.playlist= DoubleLinkedList()

    def agregar_cancion_a_playlist(self, titulo:str, artista:str, duracion:int):
        if (self.playlist._DoubleLinkedList__size) == 0:
            if duracion < 10 or duracion > 15:
                print("no es posible agregar a la playlist tiempo excedido")
                return
             
            nueva_cancion= Cancion(titulo, artista, duracion)
            self.playlist.append(nueva_cancion)
            print(f" Cancion {titulo} , artista: {artista}, { duracion}s fue agregada con exito")
            return

        
        cancion_actual = self.playlist.traverse()

        for cancion in cancion_actual:
            if cancion.value.titulo == titulo:
                print(f"No es posible agregar la cancion {titulo} ya existe")
                return
        if duracion < 10 or duracion > 15:
            print("no es posible agregar a la playlist tiempo excedido")
            return

        nueva_cancion= Cancion(titulo, artista, duracion)
        self.playlist.append(nueva_cancion)
        print(f" Cancion {titulo} , artista: {artista}, { duracion}s fue agregada con exito")


    def eliminar_cancion_de_la_playlist(self, titulo:str):
        cancion_actual = self.playlist.traverse()
        for i,cancion in  enumerate(cancion_actual):
            if cancion.value.titulo == titulo:
                self.playlist.delete_at(i)
                print(f"cancion {titulo} borrada existosamente")
                return

            
        print(f"nose encontro el {titulo} en esta playlist")

    def avanzar_a_la_siguiente_cancion(self):
        cancion_actual = self.playlist.traverse()
        for cancion in cancion_actual:
            print(f"Reproduciendo {cancion.value.titulo} -- {cancion.value.artista}")
            time.sleep(cancion.value.duracion)
            



gestor= Gestor_paylist()
gestor.agregar_cancion_a_playlist("s91", "karol g", 10)
gestor.agregar_cancion_a_playlist("milagros", "karol g", 15 )
gestor.agregar_cancion_a_playlist("romantico de lunes", " feid", 11 )
gestor.agregar_cancion_a_playlist("dia tras dia", " andres cepeda", 10 )
gestor.agregar_cancion_a_playlist("admv", " maluma", 13 )
print(gestor.playlist)
gestor.avanzar_a_la_siguiente_cancion







    


  