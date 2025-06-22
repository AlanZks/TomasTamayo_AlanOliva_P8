#------------- Imports -------------
from buscador_bruto import BuscadorBruto
from buscador_indexado import BuscadorIndexado
from indexador import Indexador
import os

#------------- Menu Principal -------------
class Cliente:
    def __init__(self):
        self.texto = []                         # Lista para almacenar el texto cargado desde el archivo
        self.indexador = None                   # Índice hash
        self.bruto = BuscadorBruto()

    def cargar_archivo(self):
        # Pide el nombre del archivo y lo carga desde la carpeta principal
        while True:
            nombre_archivo = input("Ingrese el nombre del archivo de texto (incluya la extensión .txt): ").strip()
                                                            # Permitir .txt o .TXT para evitar errores
            if nombre_archivo.lower().endswith(".txt"):
                break
            print("El nombre del archivo debe terminar en '.txt'. Intente nuevamente.")

        ruta = os.path.join("..", "..", nombre_archivo)
        print("Intentando abrir ruta:", os.path.abspath(ruta))

        try:
            archivo = open(ruta, 'r', encoding='utf-8')
            self.texto = []
            for linea in archivo:
                self.texto.append(linea)
            archivo.close()
            print("Archivo cargado con éxito.")
        except FileNotFoundError:
            print(f"Error: El archivo '{nombre_archivo}' no existe en la carpeta principal. Intente de nuevo.")
            self.texto = []
        except Exception as e:
            print("Error al abrir el archivo:", e)
            self.texto = []

    def tiempo(self):
                            # Devuelve el tiempo actual en milisegundos para medir el tiempo de búsqueda
        import time
        return time.time()

    def menu(self):
        # Menú principal del cliente interactivo
        while True:
            print("\n===== MENÚ =====")
            print("[1] Cargar archivo")
            print("[2] Búsqueda fuerza bruta")
            print("[3] Búsqueda indexada")
            print("[4] Crear índice hash")
            print("[5] Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.cargar_archivo()
            elif opcion == '2':
                patron = input("Ingrese el patrón a buscar: ")
                t0 = self.tiempo()
                resultado = self.bruto.buscar(self.texto, patron)
                t1 = self.tiempo()
                self.imprimir_resultado(resultado, t1 - t0)
            elif opcion == '3':
                if self.indexador is None:
                    print("Debe crear el índice primero.")
                else:
                    patron = input("Ingrese el patrón a buscar: ")
                    t0 = self.tiempo()
                    buscador_indexado = BuscadorIndexado()
                    resultado = buscador_indexado.buscar(self.indexador, self.texto, patron)
                    t1 = self.tiempo()
                    self.imprimir_resultado(resultado, t1 - t0)
            elif opcion == '4':
                self.indexador = Indexador()  # Crea una nueva instancia del indexador
                self.indexador.indexar(self.texto)  # Construye el índice hash a partir del texto ingresado
                print("Índice hash creado exitosamente.")
            elif opcion == '5':
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción inválida.")

    def imprimir_resultado(self, resultados, tiempo):
                                        # Imprime los resultados de la búsqueda y el tiempo de ejecución
        if len(resultados) == 0:
            print("Patrón no encontrado.")
        else:
            print("Cantidad de veces encontrado =", len(resultados))
            print()
            for linea, posicion in resultados:
                print("Linea =", linea, "- Posicion =", posicion)
        print("Tiempo de búsqueda:", round(tiempo * 1000, 3), "milisegundos" ) 
