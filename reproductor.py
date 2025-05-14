import time
from gestor_playlist import Gestor_paylist
import random

class reproductor():
    def __init__(self, gestor_playlist: Gestor_paylist):
        self.gestor_playlist = gestor_playlist
        self.playlist = gestor_playlist.playlist
        self.cancion_actual = None
    
    def iniciar_reproduccion(self):
        canciones = list(self.playlist.traverse())
        if canciones:
            self.cancion_actual = random.choice(canciones)
            print (f"REPRODUCIENDO ALEATORIAMENTE: {self.cancion_actual.value.titulo} - {self.cancion_actual.value.artista}")
            self.reproducir_actual()

    def reproducir_actual(self):
        if self.cancion_actual:
            cancion = self.cancion_actual.value
            print(f"Reproduciendo: {cancion.titulo} -- {cancion.artista}")
            time.sleep(cancion.duracion)
        

    def avanzar_a_la_siguiente_cancion(self):
        if self.cancion_actual:
            self.cancion_actual = self.cancion_actual.next
            self.reproducir_actual()
    
    
    def retroceder_cancion(self):
        if self.cancion_actual:
            self.cancion_actual = self.cancion_actual.prev
            self.reproducir_actual()

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
reproducir.iniciar_reproduccion()
reproducir.avanzar_a_la_siguiente_cancion()
reproducir.retroceder_cancion()
        