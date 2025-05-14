import time
from gestor_playlist import Gestor_paylist

class reproductor():
    def __init__(self, gestor_playlist: Gestor_paylist):
        self.gestor_playlist = gestor_playlist
        self.playlist = gestor_playlist.playlist


    def reproducir_actual(self):

        pass

    def avanzar_a_la_siguiente_cancion(self):
        cancion_actual = self.playlist.traverse()
        for cancion in cancion_actual:
            print(f"Reproduciendo {cancion.value.titulo} -- {cancion.value.artista}")
            time.sleep(cancion.value.duracion)
    
    
    def retroceder_cancion(self):
        cancion_actual = self.playlist.invtraverse()
        for cancion in cancion_actual:
            print(f"Reproduciendo {cancion.value.titulo} -- {cancion.value.artista}")
            time.sleep(cancion.value.duracion)

    def retroceder (self):
        pass

    def adelantar_tiempo(self):
        pass

    def activar_shuffle(self):
        pass
    

gestor= Gestor_paylist()
gestor.agregar_cancion_a_playlist("s91", "karol g", 10)
gestor.agregar_cancion_a_playlist("milagros", "karol g", 15 )
gestor.agregar_cancion_a_playlist("romantico de lunes", " feid", 11 )
gestor.agregar_cancion_a_playlist("dia tras dia", " andres cepeda", 10 )
gestor.agregar_cancion_a_playlist("admv", " maluma", 13 )
print(gestor.playlist)

reproducir  = reproductor(gestor)

reproducir.retroceder_cancion()
        