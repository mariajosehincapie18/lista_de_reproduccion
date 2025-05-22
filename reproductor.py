import time
import random
from gestor_playlist import Gestor_paylist
from lista_enlazada import DoubleLinkedList


class Reproductor():
    def __init__(self, gestor_playlist: Gestor_paylist):
        self.gestor_playlist = gestor_playlist
    
        self.cancion_actual = None
        
        
    
    def iniciar_reproduccion(self):
        if self.gestor_playlist.playlist.size  == 0:
            print("🚫 la lista esta vacia.")
            return
        if self.cancion_actual is None:
            self.cancion_actual = self.gestor_playlist.playlist.head
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
            print(f"⏮️ Reproduciendo cancion anterior: {cancion.titulo} -- {cancion.artista}")
            time.sleep(cancion.duracion)

    def reproducir_toda_playlist(self):
        if self.gestor_playlist.playlist.size == None:
            print("⚠️ la playlista esta vacia")
 
        print("Reproduccion playlist completa")
        cancion = self.gestor_playlist.playlist.head
        for _ in range(self.gestor_playlist.playlist.size):
            print(f" 🎵 REPRODUCIENDO: {cancion.value.titulo} |  {cancion.value.artista}")  
            time.sleep(cancion.value.duracion)
            cancion = cancion.next
    
        
    def activar_shuffle(self):
        playlist_aleatoria = []
        cancion = self.gestor_playlist.playlist.head
        for _ in  range(self.gestor_playlist.playlist.size):
            playlist_aleatoria.append(cancion.value)
            cancion = cancion.next

        random.shuffle(playlist_aleatoria)

        sub_playlis_aleatoria = DoubleLinkedList()
        for cancion in playlist_aleatoria:
            sub_playlis_aleatoria.append(cancion)

        print("🔀 Modo aleatorio activado. Reproduciendo todas las canciones")
        cancion_aleatoria = sub_playlis_aleatoria.head
        for _ in range(sub_playlis_aleatoria.size):
            print(f"🎵 REPRODUCIENDO: {cancion_aleatoria.value.titulo} -- {cancion_aleatoria.value.artista}")
            print("⏱️")
            time.sleep(cancion_aleatoria.value.duracion)
            cancion_aleatoria = cancion_aleatoria.next

    def adelantar_canciones(self, porcentaje):
        if self.cancion_actual is None:
            if self.gestor_playlist.playlist.size == 0:
                print("🚫 la playlist esta vacia")
                return
            self.cancion_actual = self.gestor_playlist.playlist.head
        
        cancion = self.cancion_actual.value
        print(f"cancion a reproducirse : {cancion.titulo}-- {cancion.artista}") 

        if porcentaje < 1 or porcentaje > 99:
            print("❌El porentaje debe estar entre 1 y 99")
            return
    
        tiempo_calculado = int((porcentaje/100)* cancion.duracion)
        print(f"⏩ ADELNTANDO {porcentaje}% de la cancion {cancion.titulo}")
        time.sleep(cancion.duracion - tiempo_calculado) 
        self.cancion_actual = self.cancion_actual.next


            
            
         
    


