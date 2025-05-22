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

        
        cancion = self.playlist.head
        for _  in  range(self.playlist.size):
            if cancion.value.titulo == titulo:
                (print(f" ❌ No es posible agregar la cancion {titulo} ya existe"))
                return
            cancion = cancion.next
            
        if duracion < 10 or duracion > 15:
            print(" ⚠️ no es posible agregar a la playlist tiempo excedido")
            return

        nueva_cancion= Cancion(titulo, artista, duracion)
        self.playlist.append(nueva_cancion)
        print(f"🎶 Cancion {titulo} , artista: {artista}, { duracion}s fue agregada con exito")


    def eliminar_cancion_de_la_playlist(self, titulo:str):
        cancion = self.playlist.head
        for i in  range(self.playlist.size):
            if cancion.value.titulo.lower() == titulo.lower():
                self.playlist.delete_at(i)
                print(f" 🗑️ cancion {titulo} borrada existosamente")
                return
            
            cancion= cancion.next

            
        print(f"🔍 No se encontro el {titulo} en esta playlist")

    def mostrar_toda_playlist(self):

        if self.playlist is None:
            print("⚠️ la playlista esta vacia")

        print("\n🎶 PLAYLIST: ")
        cancion = self.playlist.head
        for _ in range(self.playlist.size):
            print(f" 🎵 Cancion: {cancion.value.titulo} | , artista: {cancion.value.artista}, |  duracion { cancion.value.duracion}s")
            cancion= cancion.next


    def guardar_playlist(self, ruta_archivo= "playlist_principal.txt"):
        with open(ruta_archivo, "w", encoding="utf-8") as i:
            cancion = self.playlist.head
            for _ in range(self.playlist.size):
                i.write(f"{cancion.value.titulo}, {cancion.value.artista}, {cancion.value.duracion}\n")
                cancion = cancion.next
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
        

        print ("📂Ingresa los titulos de las canciones para la sub-playlsit: ")
        while True:
            titulo = input("Titulo('x' para terminar): ").strip()
            if titulo.lower() == "x":
                break

            cancion_encontrada = None
            cancion_disponible = self.playlist.head
            for _ in range(self.playlist.size):
                if cancion_disponible.value.titulo.lower() == titulo.lower():
                    original = cancion_disponible.value
                    cancion_encontrada = Cancion(original.titulo, original.artista, original.duracion)
                
                cancion_disponible = cancion_disponible.next

            if cancion_encontrada is None:
                print("⚠️ No se encontro en la playlist")
                continue

            ya_agregada = False
            cancion_ya_agregada= sub_playlist.head
            for _ in range(sub_playlist.size) :
                if cancion_ya_agregada.value.titulo.lower() == titulo.lower():
                    ya_agregada = True

                cancion_ya_agregada = cancion_ya_agregada.next
                
            
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
        
        cancion_en_sub_playlist = self.sub_playlist.head
        for _ in range(self.sub_playlist.size):
            if cancion_en_sub_playlist.value.titulo.lower() == titulo.lower():
                print("⚠️  Esta cancion ya esta el subplaylist . ")
                return
                
            cancion_en_sub_playlist = cancion_en_sub_playlist.next


        cancion_playlist_original = self.playlist_original.head
        for _ in range(self.playlist_original.size):
            if cancion_playlist_original.value.titulo.lower() == titulo.lower():
                cancion_original = cancion_playlist_original.value
                nueva_cancion = Cancion(cancion_original.titulo, cancion_original.artista, cancion_original.duracion)
                self.sub_playlist.append(nueva_cancion)

                print(f"✅ {titulo} agregada a la subplaylsit. ")
                return
            
            cancion_playlist_original = cancion_playlist_original.next
            
        print(f"❌ La cancion {titulo} no se encontro en la playlist orginal.")


    def volver_a_playlist_original(self):
        if self.sub_playlist and self.playlist != self.playlist_original:
            self.playlist = self.playlist_original
            self.sub_playlist = None
            print("🔁 Has salido de la sub playlist y vuelto a tu playlist principal.")

        else:
            print(" ⚠️ Ya estas en la playlist original")


    def generar_sub_playlist_por_tiempo(self):
        sub_playlist_por_tiempo = DoubleLinkedList()  
        cancion_actual = self.playlist.head
        for _ in range(self.playlist.size):
            verificador = cancion_actual.prev
            mayor = True
           
            if sub_playlist_por_tiempo.size == 0 :
                cancion = cancion_actual.value
                nueva_cancion = Cancion(cancion.titulo, cancion.artista, cancion.duracion)
                sub_playlist_por_tiempo.append(nueva_cancion)
            
            else:
                for _ in  range (self.playlist.size -1 ):
                    if verificador.value.duracion > cancion_actual.value.duracion:
                        mayor = False
                        

                    verificador= verificador.prev
                    
                if mayor:
                    cancion = cancion_actual.value
                    nueva_cancion = Cancion(cancion.titulo, cancion.artista, cancion.duracion)
                    sub_playlist_por_tiempo.append(nueva_cancion)
                       
                    
               
            
        cancion_actual= cancion_actual.next

        

        print("sub playlist por duraciones mayores")
        cancion_a = sub_playlist_por_tiempo.head
        for _ in range(sub_playlist_por_tiempo.size):
            print(f"{cancion_a.value.titulo}, {cancion_a.value.artista}, {cancion_a.value.duracion}s")
        cancion_a = cancion_a.next



            
                




            













    


  