# Mapa rapido del codigo

Chuleta corta para saber que archivo abrir y que funcion explicar durante la defensa.

## Segun la pregunta del profesor

| Si preguntan por... | Abrir | Explicar |
| --- | --- | --- |
| Inicio del programa | `main.py` | Importa `ejecutar_aplicacion()` y permite correr `python main.py`. |
| POO | `asistente_finanzas.py` | `class Gasto`, sus atributos y metodos. |
| Uso real de la clase | `asistente_finanzas.py` | `agregar_gasto()` crea un objeto `Gasto`. |
| JSON | `asistente_finanzas.py` | `cargar_datos()` y `guardar_datos(datos)`. |
| try/except | `asistente_finanzas.py` | `leer_float()`, `leer_entero()`, `leer_fecha_opcional()`, `leer_si_no()` y `cargar_datos()`. |
| Ciclo de corte | `asistente_finanzas.py` | `obtener_ciclo_actual(dia_corte)`. |
| Dashboard | `asistente_finanzas.py` | `mostrar_dashboard(datos)`. |
| Calculos del dashboard | `asistente_finanzas.py` | `calcular_total_gastado()` y `calcular_gastos_por_categoria()`. |
| Recursividad | `asistente_finanzas.py` | `categoria_usada_recursivamente()`. |
| Integridad referencial | `asistente_finanzas.py` | `eliminar_categoria(datos)`. |
| Menu | `asistente_finanzas.py` | `mostrar_menu_principal(datos)` y `ejecutar_aplicacion()`. |

Menu actual: opcion 6 = `Cargar datos demo actualizados`; opcion 7 = `Salir`.

## Que decir rapido

### POO

`Gasto` representa un gasto individual. Tiene `id_gasto`, `monto`, `categoria`, `descripcion` y `fecha`. Sus metodos son `convertir_a_diccionario()` para guardar en JSON y `resumen()` para mostrarlo en consola.

### JSON

El programa guarda datos persistentes en `data_finanzas.json`. `cargar_datos()` lee el archivo y `guardar_datos(datos)` lo actualiza.

### Recursividad

`categoria_usada_recursivamente()` revisa una lista de gastos. Si llega al final, retorna `False`; si encuentra la categoria, retorna `True`; si no, se llama a si misma con el siguiente indice.

### try/except

Las entradas del usuario usan `while True` y `try/except` para repetir si el dato es invalido. Esto evita que el programa se cierre por un error de entrada.

### Ciclo de corte

`obtener_ciclo_actual(dia_corte)` calcula inicio y fin del ciclo financiero usando `datetime`. El ciclo no siempre empieza el dia 1, depende del dia elegido por el usuario.

### Dashboard

`mostrar_dashboard(datos)` muestra el ciclo, presupuesto, total gastado, progreso global y gasto por categoria.

### Integridad referencial

Antes de borrar una categoria, `eliminar_categoria(datos)` revisa si esa categoria ya fue usada en gastos. Si fue usada, bloquea la eliminacion.

## Cambios en vivo

### Agregar opcion al menu

1. Editar `mostrar_menu_principal(datos)` para imprimir la opcion.
2. Editar `ejecutar_aplicacion()` para agregar un nuevo `elif`.

### Filtro por categoria

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

### Filtro por fecha

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

### Cambiar formato de dinero

Ir a `formatear_dinero(valor)`. Esa funcion centraliza como se muestran los montos.

### Cambiar barra de progreso

Ir a `construir_barra_progreso(porcentaje)`. Esa funcion convierte un porcentaje en una barra de texto.
