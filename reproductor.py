import time
import random

class Reproductor():
    def __init__(self, gestor_playlist: Gestor_paylist):
        self.gestor_playlist = gestor_playlist
        self.playlist = gestor_playlist.playlist
        self.cancion_actual = None
    
    def iniciar_reproduccion(self):
        canciones = list(self.playlist.traverse())
        if canciones:
            self.cancion_actual = random.choice(canciones)
           
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
    


