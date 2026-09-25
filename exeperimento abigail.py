#Amabilia Mayte López Cahuex, 5to P.C, sección B
import os
os.system ('cls')
import random
import time
class ExperimentoAbigail:
    def __init__(self):
        self.nombre = ""
        self.personaje = ""
        self.modo_juego = ""
        self.dificultad = ""
        self.chat_activado = False
        self.inventario = []
        self.juego_activo = True
    def iniciar(self):
        print("=" * 50)
        print("          INGRESO DEL JUGADOR          ")
        print("=" * 50)
        while True:
            reg_nombre = (
                input("¿Desea registrar su nombre de usuario? (Sí/No): ")
                .strip()
                .lower()
            )
            if reg_nombre in ["si", "sí", "s"]:
                self.nombre = input("➜ Ingrese su Nombre de Usuario: ").strip()
                if not self.nombre:
                    self.nombre = "Jugador_01"
                break
            elif reg_nombre in ["no", "n"]:
                print("Regresando a la pantalla de ingreso...")
                time.sleep(1)
            else:
                print("Opción inválida. Responda 'Sí' o 'No'.")
        print("\n--- ELEGIR PERSONAJE ---")
        print("1. Científico")
        print("2. Guardia de Seguridad")
        print("3. Superviviente")
        opc_p = input("➜ Selección (1-3): ").strip()
        personajes = {
            "1": "Científico",
            "2": "Guardia de Seguridad",
            "3": "Superviviente",
        }
        self.personaje = personajes.get(opc_p, "Superviviente")
        print("\n--- MODO DE JUEGO ---")
        print("1. Solitario")
        print("2. Multijugador Cooperativo")
        opc_m = input("➜ Selección (1-2): ").strip()
        if opc_m == "1":
            self.modo_juego = "Solitario"
            print("\n--- NIVEL DE DIFICULTAD (Solitario) ---")
            print("1. Fácil")
            print("2. Normal")
            opc_d = input("➜ Selección (1-2): ").strip()
            if opc_d == "1":
                self.dificultad = "Normal"
            else:
                self.dificultad = "Extremo"
        else:
            self.modo_juego = "Multijugador Cooperativo"
            print("\n--- NIVEL DE DIFICULTAD (Multijugador) ---")
            print("1. Fácil")
            print("2. Difícil")
            opc_d = input("➜ Selección (1-2): ").strip()
            if opc_d == "1":
                self.dificultad = "Fácil"
                print(
                    "\n[Sistema]: Conectado con el jugador en amigos..."
                )
            else:
                self.dificultad = "Difícil"
                self.chat_activado = True
                print("\n[Sistema]: Activar Chat de Juego...")
        time.sleep(1.5)
        self.exploracion_y_busqueda()
    def exploracion_y_busqueda(self):
        print("\n" + "=" * 50)
        print("      EXPLORACIÓN Y BÚSQUEDA EN EL LABORATORIO      ")
        print("=" * 50)
        while self.juego_activo:
            print("\n-> Caminando y explorando habitaciones...")
            time.sleep(1)
            suministro = random.choice(["Linterna", "Pilas", "Botiquín"])
            if suministro not in self.inventario:
                self.inventario.append(suministro)
                print(
                    f"➜ Recolectar Suministros: Has obtenido [{suministro}]"
                )
            print("➜ Buscando Llaves / Tarjetas...")
            time.sleep(1)
            if "Tarjeta de Salida" not in self.inventario:
                if random.random() < 0.4:
                    self.inventario.append("Tarjeta de Salida")
                    print("¡Encontraste la [Tarjeta de Salida]!")
            hay_monstruo = random.choice([True, False])
            if hay_monstruo:
                print("\n¡ALERTA! ¡Apareció el monstruo en la zona!")
                print("1. Esconderse")
                print("2. Disparar Arma")
                accion_m = input("➜ ¿Qué deseas hacer? (1-2): ").strip()
                if accion_m == "1":
                    print("Te escondiste con éxito del monstruo.")
                elif accion_m == "2":
                    if "Arma" in self.inventario:
                        print(
                            "Disparaste el arma y ahuyentaste al monstruo."
                        )
                    else:
                        print(
                            "No tenías un arma... ¡El monstruo te ha derrotado!"
                        )
                        self.juego_activo = False
                        break
                else:
                    print("No reaccionaste a tiempo...")
            if self.chat_activado and self.juego_activo:
                print("[Chat de Juego]: Aliado_02 - ¡Sigue buscando la tarjeta!")
            print("\nVerificando si tienes los requisitos para salir...")
            tiene_suministros = any(
                item in self.inventario
                for item in ["Linterna", "Pilas", "Botiquín"]
            )
            tiene_salida = "Tarjeta de Salida" in self.inventario
            if tiene_suministros and tiene_salida:
                print("\n" + "=" * 50)
                print(
                    f"¡FELICIDADES {self.nombre}! ENCONTRÓ SUMINISTROS Y SALIDA."
                )
                print("HAS ESCAPADO CON ÉXITO.")
                print("=" * 50)
                self.juego_activo = False
            else:
                print(
                    "Aún no cumples las condiciones (Faltan suministros o la Tarjeta). Reintentando ciclo..."
                )
                time.sleep(1.5)

if __name__ == "__main__":
    juego = ExperimentoAbigail()
    juego.iniciar()