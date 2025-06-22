#------------- TablaHash -------------


class TablaHash:
    def __init__(self, capacidad=10007):
                                            # Inicializa la tabla hash con una capacidad dada
                                            # Por defecto, la capacidad es 10007, un número primo
        self.capacidad = capacidad
        self.tabla = [[] for _ in range(self.capacidad)]

    def _hash(self, clave):
                                                 # Calcula el valor hash para una clave usando una combinación lineal (multiplicador 31)
        h = 0
        for c in clave:
            h = (h * 31 + ord(c)) % self.capacidad
        return h

    def insertar(self, clave, valor):
        pos = self._hash(clave)
        for par in self.tabla[pos]:
            if par[0] == clave:
                                                        # Si la clave ya existe, agrega el valor solo si no esta repite
                if valor not in par[1]:
                    par[1].append(valor)
                return
                                            # Si la clave no existe, la agrega junto con el valor
        self.tabla[pos].append([clave, [valor]])

    def obtener(self, clave):
        pos = self._hash(clave)
        for par in self.tabla[pos]:
            if par[0] == clave:
                return par[1]  # Retorna lista de valores asociados a la clave
        return []

    def claves(self):
                                    # Devuelve una lista con todas las claves guardadas en la tabla
        todas = []
        for cubeta in self.tabla:
            for par in cubeta:
                todas.append(par[0])
        return todas
