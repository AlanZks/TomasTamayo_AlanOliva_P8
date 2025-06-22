# Ejecución del Sistema de Búsqueda de Texto

Sigue estos pasos para ejecutar el programa correctamente:

## 1. Requisitos

- Python 3.7 o superior
- Archivo de texto (`.txt`) que desees analizar

## 2. Coloca tu archivo `.txt`

Copia el archivo de texto que quieres analizar en la carpeta principal del proyecto (donde está `main.py`).

## 3. Ejecuta el programa

En la terminal, ejecuta:

```sh
python main.py
```

## 4. Uso del menú

Al iniciar el programa, verás un menú interactivo con las siguientes opciones:

1. **Cargar archivo:** Ingresa el nombre del archivo `.txt` a analizar.
2. **Búsqueda fuerza bruta:** Realiza la búsqueda secuencial del patrón que indiques.
3. **Búsqueda indexada:** Realiza la búsqueda usando el índice hash (requiere crear el índice previamente).
4. **Crear índice hash:** Genera el índice a partir del texto cargado.
5. **Salir:** Sale del programa.

**Recomendaciones:**
- Primero carga el archivo (opción 1).
- Si quieres búsquedas rápidas, crea el índice (opción 4) antes de usar la búsqueda indexada (opción 3).
- El sistema mostrará los resultados y el tiempo de búsqueda al finalizar.

---
