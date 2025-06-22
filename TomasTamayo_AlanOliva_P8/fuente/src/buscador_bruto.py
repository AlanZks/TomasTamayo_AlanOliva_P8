#------------- Buscador Bruto -------------


class BuscadorBruto:
    def es_separador(self, c):                          # Devuelve True si el carácter es un separador 
        return not (
            (c >= "a" and c <= "z") or
            (c >= "A" and c <= "Z") or
            (c >= "0" and c <= "9") or
            (c in "áéíóúüÁÉÍÓÚÜñÑ")
        )
    #------------- Funcion Buscar Fuerza Bruta -------------
    def buscar(self, texto, patron):  # Busca ocurrencias de una palabra exacta en el texto
        resultado = []
        patron_len = len(patron)
        i = 0
        while i < len(texto):  # Recorre cada línea del texto
            linea = texto[i]
            pos = 0
            while pos <= len(linea) - patron_len:  # Busca posibles coincidencias en la línea
                coincide = True
                k = 0
                while k < patron_len:  # Compara carácter por carácter
                    if linea[pos + k] != patron[k]:
                        coincide = False
                        break
                    k += 1
                if coincide:                             # Solo cuenta coincidencia si está limitada por separadores asi facilitando la búsqueda de palabras exactas
                    antes = (pos == 0) or self.es_separador(linea[pos - 1])
                    despues = (pos + patron_len == len(linea)) or self.es_separador(
                        linea[pos + patron_len] if pos + patron_len < len(linea) else "\n"
                    )
                    if antes and despues:
                        resultado.append((i + 1, pos))
                pos += 1
            i += 1
        return resultado
