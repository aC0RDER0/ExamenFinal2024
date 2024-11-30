import random
import os

class JuegoAdivinanza:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def registrar_intento(self):
        self.intentos += 1

    def validar_numero(self):
        while True:
            prueba = input("Ingrese un número entre 1 y 100: ")
            if prueba.isnumeric():
                prueba = int(prueba)
                if prueba > 100:
                    print("Debe ser igual o menor a 100.")
                elif prueba < 1:
                    print("Debe ser igual o mayor a 1.")
                elif prueba == self.numero_secreto:
                    self.registrar_intento()
                    print(f"¡Ganaste en {self.intentos} intentos!")
                    return True
                elif prueba > self.numero_secreto:
                    print("El número secreto es menor.")
                    self.registrar_intento()
                elif prueba < self.numero_secreto:
                    print("El número secreto es mayor.")
                    self.registrar_intento()
            else:
                print("Selecciona un número válido.")

    def reiniciar(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        print("El juego ha sido reiniciado.")


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial_partidas = []

    def registrar_partida(self, intentos, gano):
        self.historial_partidas.append({"intentos": intentos, "gano": gano})

    def mostrar_estadisticas(self):
      
        partidas_jugadas = len(self.historial_partidas)
        partidas_ganadas = sum(1 for partida in self.historial_partidas if partida["gano"])

        if partidas_jugadas > 0:
            porcentaje_ganadas = (partidas_ganadas / partidas_jugadas) * 100
        else:
            porcentaje_ganadas = 0

        print(f"\nJugador: {self.nombre}")
        print(f"Partidas jugadas: {partidas_jugadas}")
        print(f"Porcentaje de partidas ganadas: {porcentaje_ganadas:.2f}%")
        print("Historial de partidas:")
        for i, partida in enumerate(self.historial_partidas, start=1):
            print(f"  Partida {i}: Intentos - {partida['intentos']}, Ganó - {'Sí' if partida['gano'] else 'No'}")

    def guardar_estadisticas(self):
        with open("estadísticas.txt", "w") as archivo:
            archivo.write(f"{self.nombre}\n")
            for partida in self.historial_partidas:
                archivo.write(f"{partida['intentos']},{partida['gano']}\n")
        print("Estadísticas guardadas en 'estadísticas.txt'.")

    def cargar_estadisticas(self):
        if os.path.exists("estadísticas.txt"):
            with open("estadísticas.txt", "r") as archivo:
                lineas = archivo.readlines()
                self.nombre = lineas[0].strip()
                self.historial_partidas = []
                for linea in lineas[1:]:
                    intentos, gano = linea.strip().split(",")
                    self.historial_partidas.append({"intentos": int(intentos), "gano": gano == "True"})
            print("Estadísticas cargadas desde 'estadísticas.txt'.")
        else:
            print("No se encontraron estadísticas previas. Iniciando nuevo jugador.")


def menu():
    
    print("Bienvenido al Juego de Adivinanza de Números")
    nombre_jugador = input("Por favor, ingresa tu nombre: ")
    jugador = Jugador(nombre_jugador)
    jugador.cargar_estadisticas()

    while True:
        opcion = input(
            "\nSelecciona una opción:\n"
            "a) Comenzar una nueva partida.\n"
            "b) Ver las estadísticas del jugador.\n"
            "c) Salir del juego.\n"
            "Opción: "
        )
        if opcion == "a":
            juego = JuegoAdivinanza()
            gano = juego.validar_numero()
            jugador.registrar_partida(juego.intentos, gano)
            juego.reiniciar()
        elif opcion == "b":
            jugador.mostrar_estadisticas()
        elif opcion == "c":
            jugador.guardar_estadisticas()
            print("¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

menu()