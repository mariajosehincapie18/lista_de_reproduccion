from lista_enlazada import DoubleLinkedList
from cancion import Cancion
import os
class Gestor_paylist:
    def __init__(self):
        self.playlist= DoubleLinkedList()
        self.playlist_original = None
        self.sub_playlist = None

    def agregar_cancion_a_playlist(self, titulo:str, artista:str, duracion:int):
        if (self.playlist.size) == 0:
            if duracion < 10 or duracion > 15:
                print(" ⚠️ no es posible agregar a la playlist tiempo excedido")
                return
             
            nueva_cancion= Cancion(titulo, artista, duracion)
            self.playlist.append(nueva_cancion)
            print(f"🎶 Cancion {titulo} , artista: {artista}, { duracion}s fue agregada con exito")
            return

        
        canciones = self.playlist.traverse()

        for cancion in canciones:
            if cancion.value.titulo == titulo:
                print(f" ❌ No es posible agregar la cancion {titulo} ya existe")
                return
        if duracion < 10 or duracion > 15:
            print(" ⚠️ no es posible agregar a la playlist tiempo excedido")
            return

        nueva_cancion= Cancion(titulo, artista, duracion)
        self.playlist.append(nueva_cancion)
        print(f"🎶 Cancion {titulo} , artista: {artista}, { duracion}s fue agregada con exito")


    def eliminar_cancion_de_la_playlist(self, titulo:str):
        canciones = self.playlist.traverse()
        for i,cancion in  enumerate(canciones):
            if cancion.value.titulo == titulo:
                self.playlist.delete_at(i)
                print(f" 🗑️ cancion {titulo} borrada existosamente")
                return

            
        print(f"🔍 No se encontro el {titulo} en esta playlist")

    def mostrar_toda_playlist(self):
        canciones = self.playlist.traverse()
        if not canciones:
            print("⚠️ la playlista esta vacia")

        print("\n🎶 PLAYLIST: ")
        for cancion in canciones:
            print(f" 🎵 Cancion: {cancion.value.titulo} | , artista: {cancion.value.artista}, |  duracion { cancion.value.duracion}s")


    def guardar_playlist(self, ruta_archivo= "playlist_principal.txt"):
        with open(ruta_archivo, "w", encoding="utf-8") as i:
            canciones = self.playlist.traverse()
            for cancion in canciones:
                i.write(f"{cancion.value.titulo}, {cancion.value.artista}, {cancion.value.duracion}\n")
        print("✅ Playlist guardada exitosamente")

    def cargar_playlist(self, ruta_archivo ="playlist_principal.txt" ):
        if not os.path.exists(ruta_archivo):    
            print("📂No hay playlist guardada aun.")
            return
        
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as i:
                for parte in i:
                    partes= parte.strip().split(",")
                    if len(partes) == 3:
                        titulo, artista, duracion = partes
                        self.playlist.append(Cancion(titulo, artista, int(duracion)))
            print("✅Playlist cargada desde el achivo")
        except FileNotFoundError:
            print("⚠️ No se encontro el archivo de playlist: ")


    def generar_sub_playlist (self):
        sub_playlist = DoubleLinkedList()  
        canciones_disponibles= list(self.playlist.traverse())

        print ("📂Ingresa los titulos de las canciones para la sub-playlsit: ")
        while True:
            titulo = input("Titulo('x' para terminar): ").strip()
            if titulo.lower() == "x":
                break

            cancion_encontrada = None
            for cancion in canciones_disponibles:
                if cancion.value.titulo.lower() == titulo.lower():
                    original = cancion.value
                    cancion_encontrada = Cancion(original.titulo, original.artista, original.duracion)

                    break

            if cancion_encontrada is None:
                print("⚠️ No se encontro en la playlist")
                continue

            ya_agregada = False
            for cancion in sub_playlist.traverse():
                if cancion.value.titulo.lower() == titulo.lower():
                    ya_agregada = True
                    break
            
            if ya_agregada:
                print("⚠️ Esta cancion ya fue agregada a la subplaylist")
            else:
                sub_playlist.append(cancion_encontrada)
                print(f"✅ '{titulo}' añadida. ")

            
        if sub_playlist.size > 0:
            self.playlist_original = self.playlist
            self.sub_playlist = sub_playlist
            self.playlist = sub_playlist
            print("🎵Subplaylist creada con exito. ")
        
        else:
            print("🚫No se agrego ninguna cancion. ")
            
        

    def agregar_cancion_a_sub_playlist(self, titulo: str):
        if not self.sub_playlist:
            print("⚠️ No estas trabajando sobre una subplaylist")
            return
        

        for cancion in self.sub_playlist.traverse():
            if cancion.value.titulo.lower() == titulo.lower():
                print("⚠️  Esa cancion ya esta el subplaylist . ")
                return
            
        for cancion in self.playlist_original.traverse():
            if cancion.value.titulo.lower() == titulo.lower().lower:
                nueva_cancion = Cancion(cancion.value.titulo, cancion.value.artista, cancion.value.duracion)
                self.sub_playlist.append(nueva_cancion)
                print(f"✅ {titulo} agregada a la subplaylsit. ")
                return
            
        print(f"❌ La cancion {titulo} no se encontro en la playlist orginal.")


    def volver_a_playlist_original(self):
        if self.sub_playlist and self.playlist != self.playlist_original:
            self.playlist = self.playlist_original
            self.sub_playlist = None
            print("🔁 Has salido de la sub playlist y vuelto a tu playlist principal.")

        else:
            print(" ⚠️ Ya estas en la playlist original")



            













    


  