# Asistente Inteligente de Finanzas y Presupuestos

## Integrantes

- Integrante 1: [Jorge Argueta, 20250362]
- Integrante 2: [Jean Pierre Boburg, 20250516
- Integrante 2: [ESCRIBIR NOMBRE COMPLETO AQUÍ]

## Problema que resuelve

El proyecto ayuda a registrar gastos personales, clasificarlos por categoria, controlar un presupuesto global y revisar un dashboard financiero desde la consola.

## Instalacion

1. Tener Python 3 instalado.
2. Abrir una terminal en la carpeta del proyecto.
3. No instalar librerias externas: el proyecto usa solo la libreria estandar de Python.

## Ejecucion

```bash
python main.py
```

Si la computadora usa `python3` como comando principal de Python, tambien puede ejecutarse asi:

```bash
python3 main.py
```

`main.py` es el punto de entrada. Importa `ejecutar_aplicacion()` desde `asistente_finanzas.py` y no duplica la logica principal.

## Opciones del menu

1. `Agregar Gasto`: permite ingresar monto, categoria, descripcion opcional y fecha.
2. `Editar Presupuesto`: actualiza el presupuesto global usado en el dashboard.
3. `Editar Fechas (Dia de corte)`: cambia el dia en que inicia el ciclo financiero.
4. `Administrar Categorias`: permite agregar categorias y eliminar solo las que no tienen gastos registrados.
5. `Historial y Correcciones`: muestra gastos del ciclo actual y permite corregir monto o eliminar gastos.
6. `Cargar datos demo actualizados`: pide confirmacion y crea datos de ejemplo con fechas dentro del ciclo actual.
7. `Salir`: guarda los datos y cierra el programa.

## Archivo de datos

La informacion se guarda en `data_finanzas.json`.

Ese archivo contiene:

- `configuracion`: presupuesto global y dia de corte.
- `categorias`: lista de categorias disponibles.
- `gastos`: lista de gastos registrados.

El programa lee el JSON con `cargar_datos()` y lo escribe con `guardar_datos(datos)`.

## Conceptos de programacion usados

- Clase `Gasto`: representa cada gasto con atributos y metodos.
- Funciones propias: el proyecto contiene varias funciones modulares con parametros y retorno.
- `if / elif / else`: se usa en menus, validaciones y decisiones del dashboard.
- `for`: se usa para recorrer gastos y categorias.
- `while`: se usa para mantener el menu y repetir entradas hasta que sean validas.
- Listas: se usan en `categorias` y `gastos`.
- Diccionarios: se usan para representar la configuracion y cada gasto guardado.
- JSON: se usa para guardar y recuperar los datos.
- `try/except`: se usa para validar entradas y proteger lectura/escritura de archivos.
- Recursividad: `categoria_usada_recursivamente()` revisa si una categoria ya fue usada.
- `datetime`: se usa para calcular el ciclo financiero actual segun el dia de corte.

## Clase Gasto

La clase `Gasto` tiene los atributos:

- `id_gasto`
- `monto`
- `categoria`
- `descripcion`
- `fecha`

Tambien tiene los metodos:

- `convertir_a_diccionario()`: convierte el objeto a diccionario para guardarlo en JSON.
- `resumen()`: genera una linea de texto para mostrar el gasto en consola.

La clase se usa de verdad en `agregar_gasto()`, donde se crea un objeto `Gasto` antes de guardarlo.

## Recursividad e integridad de categorias

La funcion `categoria_usada_recursivamente(gastos, categoria_busqueda, indice=0)` revisa la lista de gastos paso a paso.

- Caso base: si el indice llega al final de la lista, retorna `False`.
- Si encuentra la categoria, retorna `True`.
- Si no la encuentra, se llama a si misma con `indice + 1`.

Esta funcion se usa en `eliminar_categoria(datos)`. Si una categoria ya aparece en algun gasto, el programa bloquea su eliminacion para proteger el historial.

## Ejemplo de salida esperada

```text
======================================================================
ASISTENTE INTELIGENTE DE FINANZAS Y PRESUPUESTOS
======================================================================
Ciclo actual: 01/05/2026 al 31/05/2026
Presupuesto global: Q5000.00
Gastado en ciclo: Q721.50
Progreso global: [█░░░░░░░░░] 14.4%

MENU PRINCIPAL
1. Agregar Gasto
2. Editar Presupuesto
3. Editar Fechas (Dia de corte)
4. Administrar Categorias (Agregar/Eliminar)
5. Historial y Correcciones (Ver/Editar/Eliminar gastos)
6. Cargar datos demo actualizados
7. Salir
```


## Demo visual complementaria

Además del programa principal en Python, se incluye una demo visual complementaria creada en Lovable:

https://financialapp123421.lovable.app

El código principal evaluable está en Python y se ejecuta con:

python main.py
