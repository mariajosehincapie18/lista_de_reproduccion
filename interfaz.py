from gestor_playlist import Gestor_paylist
from reproductor import Reproductor

class Interfaz():

    def mostrar_menu(self):
        while True:
            print("\n🎵 BIENVENIDO A TU PLAYLIST 🎵 ")
            print("1️⃣  Agregar cancion: ")
            print("2️⃣  Mostrar playlist: ")
            print("3️⃣  Eliminar cancion: ")
            print("4️⃣  Avanzar a la siguiente cancion: ")
            print("5️⃣  Retroceder a la cancion anterior: ")
            print("6️⃣  Mostrar Cancion en reproduccion: ")
            print("7️⃣  Activar modo aleatorio: " )
            print("8️⃣  Reproducir toda la playlis: ")
            print("9️⃣  Adelantar una cancion: ")
            print("🔟  Generar una subplaylist: ")
            print("❌. Salir")

            opcion= input("Eligen una opcion: ")

            if opcion == "1":
                print("AGREGA TU NUEVA CANCION: ")
                titulo = input("Titulo: ")
                artista = input (" Artista: ")
                duracion = int(input("Duracion: "))
                gestor.agregar_cancion_a_playlist(titulo, artista, duracion)
            elif opcion == "2":
                gestor.mostrar_toda_playlist()

            elif opcion == "3":
                print("ELIMINAR CANCION: ")
                titulo = input("Ingresa el titulo a eliminar: ")
                gestor.eliminar_cancion_de_la_playlist(titulo)
            elif opcion == "4":
                if reproductor.cancion_actual is None:
                    reproductor.iniciar_reproduccion()
                else:
                    reproductor.avanzar_a_la_siguiente_cancion()
            elif opcion == "5":
                if reproductor.cancion_actual is None:
                    reproductor.iniciar_reproduccion()
                else:
                    reproductor.retroceder_cancion()
            elif opcion == "6":
                if reproductor.cancion_actual is None:
                    print("no hay ninguna cancion en reproduccion")
                else:
                    print(f"🎶 Cancion en reproducion : {reproductor.cancion_actual.value}")
            elif  opcion == "7":
                reproductor.activar_shuffle()
            elif opcion == "8":
                reproductor.reproducir_toda_playlist()
            elif opcion == "9":
                seguir = "si"
                while seguir == "si":
                    porcentaje = int(input("INGRESA EL PORCENTAJE QUE QUIERES ADELANTAR TU CANCION"))
                    reproductor.adelantar_canciones(porcentaje)
                    seguir = input("Adelantar otra cancion (si/no):  ").lower()
               

                

        

            elif opcion == "x":
                gestor.guardar_playlist()
                break



gestor = Gestor_paylist()
gestor.cargar_playlist()
reproductor = Reproductor(gestor)
interfaz = Interfaz()
interfaz.mostrar_menu()