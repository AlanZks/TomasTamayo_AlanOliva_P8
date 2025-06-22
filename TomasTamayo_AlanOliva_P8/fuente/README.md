# Sistema de Búsqueda de Texto

Este proyecto implementa un sistema de búsqueda de texto en archivos `.txt`, con dos estrategias: búsqueda por fuerza bruta y búsqueda indexada usando una tabla hash. Permite cargar archivos, crear un índice de palabras y buscar patrones de manera eficiente.

## Estructura del Proyecto

- `main.py`: Punto de entrada de la aplicación.
- `cliente.py`: Controlador principal e interfaz de usuario.
- `buscador_bruto.py`: Implementa la búsqueda secuencial (fuerza bruta).
- `buscador_indexado.py`: Implementa la búsqueda optimizada mediante índice hash.
- `indexador.py`: Construye el índice invertido sobre el texto usando una tabla hash.
- `tabla_hash.py`: Estructura de datos hash personalizada para indexar palabras.

## Requisitos

- Python 3.7 o superior.

## Instalación

1. Asegúrate de tener tus archivos `.txt` en el directorio raíz del proyecto o sube el archivo que deseas analizar.

No se requieren librerías externas; todo el código es Python puro.

## Ejecución

Para iniciar la aplicación, ejecuta:

```sh
python main.py
```

A continuación, verás un menú interactivo con las siguientes opciones:

1. **Cargar archivo:** Ingresa el nombre del archivo `.txt` a analizar.
2. **Búsqueda fuerza bruta:** Busca un patrón recorriendo todo el texto secuencialmente.
3. **Búsqueda indexada:** Busca un patrón usando un índice hash (requiere crear el índice primero).
4. **Crear índice hash:** Genera un índice de palabras a partir del texto cargado.
5. **Salir:** Termina el programa.

**Recomendaciones:**
- Antes de usar la búsqueda indexada, debes crear el índice (opción 4) luego de cargar un archivo.
- El sistema reporta el tiempo de búsqueda y las posiciones encontradas.

> **Nota importante:**  
> Si el programa es utilizado desde un editor de código (por ejemplo, Visual Studio Code, PyCharm u otros), se recomienda ejecutar el archivo `main.py` directamente desde la carpeta que contiene el código fuente (`fuente` o `src`) y **no desde la carpeta principal del proyecto**.  
>
> Esto se debe a que, dependiendo del editor y la configuración utilizada, la ruta de trabajo puede variar, lo que podría provocar errores al intentar cargar los archivos `.txt`.  
>
> Si experimenta problemas al cargar o localizar los archivos de texto, asegúrese de abrir una terminal en la carpeta `fuente` (o `src`) y ejecutar el programa desde allí con el siguiente comando:
>
> ```bash
> python main.py
> ```
>
> De este modo, se garantiza que el programa pueda acceder correctamente a los archivos necesarios para su funcionamiento.

## Ejemplo de uso

1. Selecciona la opción 1 y carga tu archivo `.txt`.
2. Si deseas una búsqueda rápida, selecciona la opción 4 para crear el índice.
3. Usa la opción 3 para realizar búsquedas indexadas o la opción 2 para búsquedas por fuerza bruta.
4. Observa los resultados y el tiempo de ejecución mostrados en pantalla.

---

## Autores

- Tomás Tamayo
- Alan Oliva