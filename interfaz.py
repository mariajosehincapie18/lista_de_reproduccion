from gestor_playlist import Gestor_paylist

class Interfaz():

    def mostrar_menu(self):
        while True:
            print("\n🎵 MENU PRINCIPAL 🎵 ")
            print("1. Agregar cancion")
            print("2. Mostrar playlist")
            print(" 3. Eliminar cancion")
            print("4. Salir")

            opcion= input("Eligen una opcion: ")

            if opcion == "1":
                titulo = input("Titulo: ")
                artista = input (" Artista: ")
                duracion = int(input("Duracion: "))
                gestor.agregar_cancion_a_playlist(titulo, artista, duracion)
            elif opcion == "2":
                gestor.mostrar_toda_playlist()

            elif opcion == "3":
                titulo = input("Ingresa el titulo a eliminar: ")
                gestor.eliminar_cancion_de_la_playlist(titulo)

            elif opcion == "4":
                gestor.guardar_playlist()
                break



gestor = Gestor_paylist()
gestor.cargar_playlist()
interfaz = Interfaz()
interfaz.mostrar_menu()