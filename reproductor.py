import time
import random
from gestor_playlist import Gestor_paylist

class Reproductor():
    def __init__(self, gestor_playlist: Gestor_paylist):
        self.gestor_playlist = gestor_playlist
        self.playlist = gestor_playlist.playlist
        self.cancion_actual = None
        
        
    
    def iniciar_reproduccion(self):
        if self.gestor_playlist.playlist.size  == 0:
            print("🚫 la lista esta vacia.")
            return
        if self.cancion_actual is None:
            self.cancion_actual = next(self.gestor_playlist.playlist.traverse())
            cancion= self.cancion_actual.value
            print(f"▶️ REPRODUCIENDO: {cancion.titulo} -- {cancion.artista}")
            time.sleep(cancion.duracion)
        

    def reproducir_actual(self):
        if self.cancion_actual:
            cancion = self.cancion_actual.value
            print(f"Reproduciendo: {cancion.titulo} -- {cancion.artista}")
            time.sleep(cancion.duracion)
        else:
            print("🚫 No hay cancion en reproduccion")
        

    def avanzar_a_la_siguiente_cancion(self):
        if self.cancion_actual is None:
            self.iniciar_reproduccion()
            return
        else:
            self.cancion_actual = self.cancion_actual.next
            cancion = self.cancion_actual.value
            print(f"⏭️ Reproduciendo: {cancion.titulo} -- {cancion.artista}")
            time.sleep(cancion.duracion)
            
        

    
    def retroceder_cancion(self):
        if self.cancion_actual is None:
            self.iniciar_reproduccion()
            return
        
        else:
            self.cancion_actual = self.cancion_actual.prev
            cancion = self.cancion_actual.value
            print(f"⏭️ Reproduciendo cancion anterior: {cancion.titulo} -- {cancion.artista}")
            time.sleep(cancion.duracion)

    def reproducir_toda_playlist(self):
        canciones = self.playlist.traverse()
        if not canciones:
            print("⚠️ la playlista esta vacia")
 
        print("Reproduccion playlist completa")
        for cancion in canciones:
            print(f" 🎵 REPRODUCIENDO: {cancion.value.titulo} |  {cancion.value.artista}")  
            time.sleep(cancion.value.duracion)
    
        
    def activar_shuffle(self):
        playlist_aleatoria = []
        for cancion in  self.gestor_playlist.playlist.traverse():
            playlist_aleatoria.append(cancion.value)

        random.shuffle(playlist_aleatoria)

        print("🔀 Modo aleatorio activado. Reproduciendo todas las canciones")
        for cancion in playlist_aleatoria:
            print(f"🎵 REPRODUCIENDO: {cancion.titulo} -- {cancion.artista}")
            print("⏱️")
            time.sleep(cancion.duracion)

    def adelantar_canciones(self, porcentaje):
        if self.cancion_actual is None:
            if self.gestor_playlist.playlist.size == 0:
                print("🚫 la playlist esta vacia")
                return
            self.cancion_actual = next(self.gestor_playlist.playlist.traverse())
        
        cancion = self.cancion_actual.value
        print(f"cancion a reproducirse : {cancion.titulo}-- {cancion.artista}") 

        if porcentaje < 1 or porcentaje > 99:
            print("❌El porentaje debe estar entre 1 y 99")
            return
    
        tiempo_calculado = int((porcentaje/100)* cancion.duracion)
        print(f"⏩ ADELNTANDO {porcentaje}% de la cancion {cancion.titulo}")
        time.sleep(cancion.duracion - tiempo_calculado)

        if self.cancion_actual.next:
            self.cancion_actual = self.cancion_actual.next


            
            
         
    


