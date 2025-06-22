from tabla_hash import TablaHash

#------------- Indexador -------------

class Indexador:
    def __init__(self):
        self.indice = TablaHash()  # Inicializa una tabla hash para almacenar el índice de palabras

    def es_alfanumerico(self, c):
                                                                # Retorna True si el carácter es letra o número
        return (
            (c >= "a" and c <= "z") or
            (c >= "A" and c <= "Z") or
            (c >= "0" and c <= "9") or
            (c in "áéíóúüÁÉÍÓÚÜñÑ")
        )

    def limpiar_palabra(self, palabra):
        # Elimina caracteres no alfanuméricos al inicio y final de la palabra (limpia puntos o comas)
        inicio = 0
        fin = len(palabra) - 1
        while inicio <= fin and not self.es_alfanumerico(palabra[inicio]):
            inicio += 1
        while fin >= inicio and not self.es_alfanumerico(palabra[fin]):
            fin -= 1
        return palabra[inicio:fin+1]

    def indexar(self, texto):
                                        # Recorre todo el texto línea por línea y extrae palabras para indexarlas
        i = 0
        while i < len(texto):
            linea = texto[i]
            palabra = ""
            j = 0
            while j <= len(linea):
                                                        # Cuando encuentra separador o fin de línea donde procesa la palabra encontrada
                if j == len(linea) or linea[j] == " " or linea[j] == "\n" or linea[j] == "\t":
                    if len(palabra) > 0:
                        palabra_limpia = self.limpiar_palabra(palabra)
                        if palabra_limpia != "":
                            self.indice.insertar(palabra_limpia, i)  # Inserta palabra y número de línea
                        palabra = ""
                else:
                    palabra += linea[j]
                j += 1
            i += 1

    def obtener_lineas(self, palabra):
        # Devuelve las líneas donde aparece la palabra limpia (sin signos)
        palabra_limpia = self.limpiar_palabra(palabra)
        return self.indice.obtener(palabra_limpia)
