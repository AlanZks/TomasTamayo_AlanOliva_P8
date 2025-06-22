#------------- Buscador Indexado -------------


class BuscadorIndexado:
    def es_separador(self, c):              # Retorna True si el carácter es un separador 
        return not (
            (c >= "a" and c <= "z") or
            (c >= "A" and c <= "Z") or
            (c >= "0" and c <= "9") or
            (c in "áéíóúüÁÉÍÓÚÜñÑ")
        )
#------------- Funcion Buscar De Indexado -------------
    def buscar(self, indexador, texto, patron):
        palabras = []     # Lista para almacenar las palabras del patrón (por si es una frase)
        palabra = ""
        i = 0
        # Separa el patrón en palabras usando espacios
        while i <= len(patron):
            if i == len(patron) or patron[i] == " ":
                if len(palabra) > 0:
                    palabras.append(palabra)
                    palabra = ""
            else:
                palabra += patron[i]
            i += 1

        if len(palabras) == 0:
            return []

        # Busca líneas candidatas en el índice según las palabras del patrón
        if len(palabras) == 1:
            lineas_candidatas = indexador.obtener_lineas(palabras[0])
        else:
                                                    # Interseca las líneas candidatas donde aparecen todas las palabras del patrón buscado
            lineas_candidatas = indexador.obtener_lineas(palabras[0])
            j = 1
            while j < len(palabras):
                siguientes = indexador.obtener_lineas(palabras[j])
                temp = []
                for x in lineas_candidatas:
                    for y in siguientes:
                        if x == y and x not in temp:
                            temp.append(x)
                lineas_candidatas = temp
                j += 1

        resultado = []
                                            # Por cada línea candidata, busca coincidencias exactas del patrón
        for idx in lineas_candidatas:
            linea = texto[idx]
            pos = 0
            patron_len = len(patron)
            while pos <= len(linea) - patron_len:
                coincide = True
                k = 0
                while k < patron_len:
                    if linea[pos + k] != patron[k]:
                        coincide = False
                        break
                    k += 1
                if coincide:
                                                                        # Solo cuenta si está limitada por separadores (palabra exacta)
                    antes = (pos == 0) or self.es_separador(linea[pos - 1])
                    despues = (pos + patron_len == len(linea)) or self.es_separador(
                        linea[pos + patron_len] if pos + patron_len < len(linea) else "\n"
                    )
                    if antes and despues:
                        resultado.append((idx + 1, pos))
                pos += 1
        resultado.sort()
        return resultado
