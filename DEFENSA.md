# Guia de defensa

## A. Problema en una frase

"Mi programa ayuda a registrar gastos personales, clasificarlos por categoría y controlar un presupuesto global dentro de un ciclo financiero personalizado."

## B. Frase tecnica

"El proyecto usa una clase Gasto, funciones modulares, listas y diccionarios, persistencia en JSON, validaciones con try/except, menú con while, cálculos con for, decisiones con if/elif/else y una función recursiva para proteger categorías usadas."

## C. Que hace cada archivo

- `main.py`: punto de entrada del programa. Importa `ejecutar_aplicacion()` desde `asistente_finanzas.py`.
- `asistente_finanzas.py`: contiene la clase `Gasto`, las funciones, el menu, el dashboard, validaciones y manejo del JSON.
- `data_finanzas.json`: guarda configuracion, categorias y gastos.
- `README.md`: explica instalacion, ejecucion, uso del menu y conceptos de programacion usados.
- `DEFENSA.md`: guia para explicar el proyecto en la presentacion.
- `requirements.txt`: indica que no hay dependencias externas.
- `.gitignore`: evita subir archivos temporales como `__pycache__/`, `*.pyc`, `.venv/`, `.env` y `.DS_Store`.

## D. Mapa rapido del codigo

### Si me piden explicar algo del codigo, ¿a donde voy?

1. Si preguntan donde empieza el programa:
   - Ir a `main.py`.
   - Explicar que importa `ejecutar_aplicacion` desde `asistente_finanzas.py`.
   - Decir que esto permite ejecutar el proyecto con `python main.py`.

2. Si preguntan por Programacion Orientada a Objetos:
   - Ir a `class Gasto`.
   - Explicar que representa un gasto individual.
   - Explicar atributos: `id_gasto`, `monto`, `categoria`, `descripcion`, `fecha`.
   - Explicar metodos: `convertir_a_diccionario()` y `resumen()`.
   - Ir a `agregar_gasto()` y mostrar que ahi se crea un objeto `Gasto` real.

3. Si preguntan por JSON:
   - Ir a `cargar_datos()`.
   - Ir a `guardar_datos(datos)`.
   - Explicar que el programa usa `data_finanzas.json` para guardar configuracion, categorias y gastos.

4. Si preguntan por manejo de errores:
   - Ir a funciones de lectura como `leer_float()`, `leer_entero()`, `leer_fecha_opcional()` y `leer_si_no()`.
   - Explicar que usan `while True` y `try/except` para no colapsar si el usuario escribe algo invalido.
   - Tambien mencionar `cargar_datos()`, porque protege si el JSON no existe o esta dañado.

5. Si preguntan por dashboard:
   - Ir a `mostrar_dashboard(datos)`.
   - Explicar que muestra ciclo actual, presupuesto, total gastado, barra visual y gastos por categoria.
   - Mencionar `calcular_total_gastado()` y `calcular_gastos_por_categoria()`.

6. Si preguntan por dia de corte:
   - Ir a `obtener_ciclo_actual(dia_corte)`.
   - Explicar que calcula fecha inicial y fecha final del ciclo financiero usando `datetime`.

7. Si preguntan por recursividad:
   - Ir a `categoria_usada_recursivamente(gastos, categoria_busqueda, indice=0)`.
   - Explicar:
     - Caso base: si `indice` llega al final de la lista, retorna `False`.
     - Si encuentra la categoria, retorna `True`.
     - Si no la encuentra, se llama a si misma con `indice + 1`.

8. Si preguntan por integridad referencial:
   - Ir a `eliminar_categoria(datos)`.
   - Explicar que antes de borrar una categoria se revisa si ya fue usada en gastos.
   - Si `categoria_usada_recursivamente()` devuelve `True`, se bloquea la eliminacion.
   - Ejemplo: no se puede borrar "Comida" si hay un gasto registrado con categoria "Comida".

## E. Si me piden cambiar algo en vivo

1. Agregar una nueva opcion al menu:
   - Ir a `mostrar_menu_principal(datos)` para imprimir la nueva opcion.
   - Ir a `ejecutar_aplicacion()` para agregar el nuevo `elif`.
   - Explicar que el menu se muestra en una funcion y la accion se ejecuta en otra.
   - En el menu actual, la opcion 6 carga datos demo actualizados y la opcion 7 sale del programa.

2. Agregar filtro por categoria:

```python
def filtrar_gastos_por_categoria(gastos, categoria):
    gastos_filtrados = []

    for gasto in gastos:
        try:
            if gasto["categoria"].strip().lower() == categoria.strip().lower():
                gastos_filtrados.append(gasto)
        except Exception:
            pass

    return gastos_filtrados
```

Esta funcion recorre la lista de gastos y retorna solo los que coinciden con la categoria.

3. Agregar filtro por fecha:

```python
def filtrar_gastos_por_fecha(gastos, fecha_buscada):
    gastos_filtrados = []

    for gasto in gastos:
        try:
            if gasto["fecha"] == fecha_buscada:
                gastos_filtrados.append(gasto)
        except Exception:
            pass

    return gastos_filtrados
```

4. Cambiar formato de dinero:
   - Ir a `formatear_dinero(valor)`.
   - Explicar que esa funcion centraliza como se muestran los montos en quetzales.

5. Cambiar barra de progreso:
   - Ir a `construir_barra_progreso(porcentaje)`.
   - Explicar que convierte un porcentaje en una barra visual de texto.

6. Agregar un nuevo campo a los gastos:
   - Tocar `class Gasto`.
   - Tocar `agregar_gasto()`.
   - Tocar `asegurar_estructura()`.
   - Tocar `imprimir_gasto()`.

## F. Guion de presentacion de 5 a 7 minutos

1. Problema:
   "Muchas personas gastan durante el mes sin tener claro cuanto llevan acumulado ni en que categorias se les va mas dinero."

2. Solucion:
   "Creamos un asistente de consola que registra gastos, calcula el ciclo financiero, clasifica por categoria y guarda todo en JSON."

3. Demo:
   - Ejecutar `python main.py`.
   - Mostrar dashboard.
   - Cargar datos demo actualizados si hace falta.
   - Agregar un gasto.
   - Mostrar historial.
   - Intentar borrar una categoria usada y demostrar que el programa lo bloquea.

4. Codigo:
   - `main.py`.
   - `class Gasto`.
   - `agregar_gasto()`.
   - `cargar_datos()` y `guardar_datos()`.
   - `obtener_ciclo_actual()`.
   - `categoria_usada_recursivamente()`.
   - `eliminar_categoria()`.

## G. Respuesta si preguntan por uso de IA

"Sí usamos IA como apoyo, pero revisamos y adaptamos el código a los requisitos del curso. La lógica está en Python estándar, sin dependencias externas, y puedo explicar las partes principales: clase Gasto, JSON, validaciones, ciclo de corte, dashboard y recursividad."

## H. Checklist final

[ ] Borre archivos .pyc
[ ] Existe .gitignore
[ ] Llene nombres en README.md
[ ] Probe python main.py
[ ] Probe cargar datos demo actualizados
[ ] Probe agregar gasto
[ ] Probe historial
[ ] Probe borrar categoria usada y se bloquea
[ ] Probe borrar categoria nueva sin gastos y si se elimina
[ ] Revise DEFENSA.md
[ ] Hice commits pequeños
[ ] Subi a GitHub
[ ] Copie link del repo para MIU
