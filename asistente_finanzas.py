import json
import os
import datetime


ARCHIVO_DATOS = "data_finanzas.json"
RUTA_DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), ARCHIVO_DATOS)

CATEGORIAS_BASE = [
    "Salud",
    "Amigos",
    "Comida",
    "Educación",
    "Transporte",
    "Negocios",
    "Familia",
    "Ocio personal",
    "Ropa y accesorios",
    "Caridad"
]

ANCHO_BARRA = 10


class Gasto:
    """Representa un gasto con sus datos principales y metodos de apoyo."""

    def __init__(self, id_gasto, monto, categoria, descripcion, fecha):
        self.id_gasto = id_gasto
        self.monto = monto
        self.categoria = categoria
        self.descripcion = descripcion
        self.fecha = fecha

    def convertir_a_diccionario(self):
        """Convierte el objeto Gasto al formato usado en el archivo JSON."""
        gasto = {
            "id": self.id_gasto,
            "monto": self.monto,
            "categoria": self.categoria,
            "descripcion": self.descripcion,
            "fecha": self.fecha
        }

        return gasto

    def resumen(self):
        """Devuelve una descripcion corta del gasto para mostrar en consola."""
        texto = "ID " + str(self.id_gasto)
        texto = texto + " | " + str(self.fecha)
        texto = texto + " | " + str(self.categoria)
        texto = texto + " | " + formatear_dinero(self.monto)

        if self.descripcion != "":
            texto = texto + " | " + str(self.descripcion)

        return texto


def imprimir_linea():
    print("=" * 70)


def imprimir_titulo(titulo):
    print()
    imprimir_linea()
    print(titulo)
    imprimir_linea()


def formatear_dinero(valor):
    try:
        return "Q" + "{:.2f}".format(float(valor))
    except Exception:
        return "Q0.00"


def formatear_porcentaje(valor):
    try:
        valor = float(valor)

        if valor == int(valor):
            return str(int(valor)) + "%"

        return "{:.1f}%".format(valor)
    except Exception:
        return "0%"


def formatear_fecha(fecha):
    try:
        dia = str(fecha.day).zfill(2)
        mes = str(fecha.month).zfill(2)
        anio = str(fecha.year)
        return dia + "/" + mes + "/" + anio
    except Exception:
        return "00/00/0000"


def convertir_texto_a_fecha(texto):
    try:
        partes = texto.strip().split("/")

        if len(partes) != 3:
            raise ValueError

        dia = int(partes[0])
        mes = int(partes[1])
        anio = int(partes[2])

        # datetime.date hace la validacion matematica de calendario:
        # rechaza fechas imposibles como 31/02/2026 o 15/13/2026.
        return datetime.date(anio, mes, dia)
    except Exception:
        raise ValueError


def leer_texto(mensaje, permitir_vacio=False):
    while True:
        try:
            texto = input(mensaje).strip()

            if texto == "" and permitir_vacio:
                return ""

            if texto == "":
                print("[!] Este campo no puede quedar vacio.")
                continue

            return texto
        except EOFError:
            print()
            print("[!] Entrada finalizada. Cerrando el programa de forma segura.")
            raise SystemExit
        except Exception:
            print("[!] Entrada invalida. Intenta de nuevo.")


def leer_float(mensaje, minimo=None):
    while True:
        try:
            texto = input(mensaje).strip()
            texto = texto.replace(",", ".")
            valor = float(texto)

            if minimo is not None and valor < minimo:
                print("[!] El monto debe ser mayor o igual a " + str(minimo) + ".")
                continue

            return valor
        except EOFError:
            print()
            print("[!] Entrada finalizada. Cerrando el programa de forma segura.")
            raise SystemExit
        except Exception:
            print("[!] Ingresa un monto numerico valido. Ejemplo: 150.75")


def leer_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            texto = input(mensaje).strip()
            valor = int(texto)

            if minimo is not None and valor < minimo:
                print("[!] El numero debe ser mayor o igual a " + str(minimo) + ".")
                continue

            if maximo is not None and valor > maximo:
                print("[!] El numero debe ser menor o igual a " + str(maximo) + ".")
                continue

            return valor
        except EOFError:
            print()
            print("[!] Entrada finalizada. Cerrando el programa de forma segura.")
            raise SystemExit
        except Exception:
            print("[!] Ingresa un numero entero valido.")


def leer_fecha_opcional(mensaje):
    while True:
        try:
            texto = input(mensaje).strip()

            if texto == "":
                return formatear_fecha(datetime.date.today())

            fecha = convertir_texto_a_fecha(texto)
            return formatear_fecha(fecha)
        except EOFError:
            print()
            print("[!] Entrada finalizada. Cerrando el programa de forma segura.")
            raise SystemExit
        except Exception:
            print("[!] Fecha invalida. Usa DD/MM/AAAA. Ejemplo: 05/05/2026")


def leer_si_no(mensaje):
    while True:
        try:
            respuesta = input(mensaje).strip().lower()

            if respuesta == "s" or respuesta == "n":
                return respuesta

            print("[!] Responde solo con s o n.")
        except EOFError:
            print()
            print("[!] Entrada finalizada. Cerrando el programa de forma segura.")
            raise SystemExit
        except Exception:
            print("[!] Entrada invalida. Responde con s o n.")


def pausar():
    try:
        print()
        input("Presiona ENTER para continuar...")
    except (EOFError, KeyboardInterrupt):
        pass
    except Exception:
        pass


def crear_copia_categorias_base():
    categorias = []

    for categoria in CATEGORIAS_BASE:
        categorias.append(categoria)

    return categorias


def crear_datos_iniciales(presupuesto_global, dia_corte):
    datos = {
        "configuracion": {
            "presupuesto_global": float(presupuesto_global),
            "dia_corte": int(dia_corte)
        },
        "categorias": crear_copia_categorias_base(),
        "gastos": []
    }

    return datos


def guardar_datos(datos):
    """Guarda el diccionario principal del programa en data_finanzas.json."""
    try:
        archivo = open(RUTA_DATOS, "w", encoding="utf-8")
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
        archivo.close()
    except Exception:
        print("[!] No se pudo guardar la informacion en " + ARCHIVO_DATOS + ".")


def obtener_numero_desde_id(id_gasto):
    try:
        return int(id_gasto)
    except Exception:
        pass

    try:
        texto = str(id_gasto)
        solo_numeros = ""

        for caracter in texto:
            if caracter >= "0" and caracter <= "9":
                solo_numeros = solo_numeros + caracter

        if solo_numeros == "":
            return 0

        return int(solo_numeros)
    except Exception:
        return 0


def categoria_existe(datos, nombre):
    try:
        nombre_limpio = nombre.strip().lower()

        for categoria in datos["categorias"]:
            if categoria.strip().lower() == nombre_limpio:
                return True

        return False
    except Exception:
        return False


def agregar_categoria_si_falta(datos, nombre):
    try:
        nombre = nombre.strip()

        if nombre == "":
            return

        if not categoria_existe(datos, nombre):
            datos["categorias"].append(nombre)
    except Exception:
        pass


def asegurar_estructura(datos):
    """Valida y completa las llaves basicas que necesita el programa."""
    try:
        if not isinstance(datos, dict):
            return crear_datos_iniciales(1.0, 1)

        if "configuracion" not in datos or not isinstance(datos["configuracion"], dict):
            datos["configuracion"] = {}

        if "presupuesto_global" not in datos["configuracion"]:
            datos["configuracion"]["presupuesto_global"] = 1.0

        try:
            datos["configuracion"]["presupuesto_global"] = float(datos["configuracion"]["presupuesto_global"])
            if datos["configuracion"]["presupuesto_global"] <= 0:
                datos["configuracion"]["presupuesto_global"] = 1.0
        except Exception:
            datos["configuracion"]["presupuesto_global"] = 1.0

        if "dia_corte" not in datos["configuracion"]:
            datos["configuracion"]["dia_corte"] = 1

        try:
            datos["configuracion"]["dia_corte"] = int(datos["configuracion"]["dia_corte"])
            if datos["configuracion"]["dia_corte"] < 1 or datos["configuracion"]["dia_corte"] > 28:
                datos["configuracion"]["dia_corte"] = 1
        except Exception:
            datos["configuracion"]["dia_corte"] = 1

        if "categorias" not in datos or not isinstance(datos["categorias"], list):
            datos["categorias"] = crear_copia_categorias_base()

        categorias_limpias = []
        for categoria in datos["categorias"]:
            try:
                nombre = str(categoria).strip()

                if nombre == "":
                    continue

                repetida = False
                for categoria_guardada in categorias_limpias:
                    if categoria_guardada.lower() == nombre.lower():
                        repetida = True

                if not repetida:
                    categorias_limpias.append(nombre)
            except Exception:
                pass

        if len(categorias_limpias) == 0:
            categorias_limpias = crear_copia_categorias_base()

        datos["categorias"] = categorias_limpias

        if "gastos" not in datos or not isinstance(datos["gastos"], list):
            datos["gastos"] = []

        gastos_limpios = []
        mayor_id = 0

        for gasto in datos["gastos"]:
            try:
                if not isinstance(gasto, dict):
                    continue

                id_actual = obtener_numero_desde_id(gasto.get("id", 0))

                if id_actual <= 0:
                    id_actual = mayor_id + 1

                if id_actual > mayor_id:
                    mayor_id = id_actual

                monto = float(gasto.get("monto", 0))

                if monto <= 0:
                    continue

                categoria = str(gasto.get("categoria", "")).strip()

                if categoria == "" and "categorias" in gasto:
                    try:
                        categorias_antiguas = gasto["categorias"]
                        if isinstance(categorias_antiguas, list) and len(categorias_antiguas) > 0:
                            categoria = str(categorias_antiguas[0]).strip()
                    except Exception:
                        categoria = ""

                if categoria == "":
                    continue

                agregar_categoria_si_falta(datos, categoria)

                descripcion = str(gasto.get("descripcion", "")).strip()
                fecha = str(gasto.get("fecha", formatear_fecha(datetime.date.today()))).strip()

                try:
                    fecha = formatear_fecha(convertir_texto_a_fecha(fecha))
                except Exception:
                    fecha = formatear_fecha(datetime.date.today())

                gasto_limpio = {
                    "id": id_actual,
                    "monto": monto,
                    "categoria": categoria,
                    "descripcion": descripcion,
                    "fecha": fecha
                }
                gastos_limpios.append(gasto_limpio)
            except Exception:
                pass

        datos["gastos"] = gastos_limpios
        return datos
    except Exception:
        return crear_datos_iniciales(1.0, 1)


def cargar_datos():
    """Lee data_finanzas.json y retorna los datos listos para usarse."""
    if not os.path.exists(RUTA_DATOS):
        return None

    try:
        archivo = open(RUTA_DATOS, "r", encoding="utf-8")
        datos = json.load(archivo)
        archivo.close()
        datos = asegurar_estructura(datos)
        guardar_datos(datos)
        return datos
    except Exception:
        print("[!] El archivo " + ARCHIVO_DATOS + " no se pudo leer correctamente.")
        print("[!] Se iniciara una configuracion nueva para que el programa no se detenga.")
        return None


def onboarding_dia_cero():
    imprimir_titulo("DIA CERO - CONFIGURACION INICIAL")
    print("No se encontro " + ARCHIVO_DATOS + " o no se pudo leer correctamente.")
    print("Se creara una configuracion nueva.")
    print("Las categorias base se cargaran automaticamente.")
    print()

    presupuesto_global = leer_float("Presupuesto Global Q: ", 0.01)
    dia_corte = leer_entero("Dia de corte mensual (1-28): ", 1, 28)

    datos = crear_datos_iniciales(presupuesto_global, dia_corte)
    guardar_datos(datos)

    print("[OK] Configuracion inicial guardada.")
    return datos


def obtener_mes_siguiente(anio, mes):
    if mes == 12:
        return anio + 1, 1

    return anio, mes + 1


def obtener_mes_anterior(anio, mes):
    if mes == 1:
        return anio - 1, 12

    return anio, mes - 1


def obtener_ciclo_actual(dia_corte):
    """Retorna la fecha inicial y final del ciclo financiero actual."""
    hoy = datetime.date.today()

    # El ciclo rodante depende del dia de corte, no del dia 1.
    # Si hoy ya llego al dia de corte, el ciclo empezo este mes.
    # Si hoy todavia esta antes del corte, el ciclo empezo el mes anterior.
    if hoy.day >= dia_corte:
        inicio_ciclo = datetime.date(hoy.year, hoy.month, dia_corte)
        anio_siguiente, mes_siguiente = obtener_mes_siguiente(hoy.year, hoy.month)
        proximo_corte = datetime.date(anio_siguiente, mes_siguiente, dia_corte)
    else:
        anio_anterior, mes_anterior = obtener_mes_anterior(hoy.year, hoy.month)
        inicio_ciclo = datetime.date(anio_anterior, mes_anterior, dia_corte)
        proximo_corte = datetime.date(hoy.year, hoy.month, dia_corte)

    # El final del ciclo es exactamente un dia antes del proximo corte.
    # Por eso se resta datetime.timedelta(days=1).
    fin_ciclo = proximo_corte - datetime.timedelta(days=1)
    return inicio_ciclo, fin_ciclo


def gasto_pertenece_al_ciclo(gasto, inicio_ciclo, fin_ciclo):
    try:
        fecha_gasto = convertir_texto_a_fecha(gasto["fecha"])

        if fecha_gasto >= inicio_ciclo and fecha_gasto <= fin_ciclo:
            return True

        return False
    except Exception:
        return False


def obtener_gastos_del_ciclo(datos):
    gastos_ciclo = []

    try:
        dia_corte = datos["configuracion"]["dia_corte"]
        inicio_ciclo, fin_ciclo = obtener_ciclo_actual(dia_corte)

        for gasto in datos["gastos"]:
            if gasto_pertenece_al_ciclo(gasto, inicio_ciclo, fin_ciclo):
                gastos_ciclo.append(gasto)
    except Exception:
        pass

    return gastos_ciclo


def calcular_total_gastado(gastos):
    """Suma los montos de una lista de gastos y retorna el total."""
    total = 0.0

    for gasto in gastos:
        try:
            total = total + float(gasto["monto"])
        except Exception:
            pass

    return total


def calcular_gastos_por_categoria(datos, gastos_ciclo):
    """Retorna un diccionario con el total gastado por cada categoria."""
    gastos_por_categoria = {}

    for categoria in datos["categorias"]:
        gastos_por_categoria[categoria] = 0.0

    for gasto in gastos_ciclo:
        try:
            categoria = gasto["categoria"]

            if categoria not in gastos_por_categoria:
                gastos_por_categoria[categoria] = 0.0

            gastos_por_categoria[categoria] = gastos_por_categoria[categoria] + float(gasto["monto"])
        except Exception:
            pass

    return gastos_por_categoria


def cargar_datos_demo_actualizados():
    """Crea datos de ejemplo con fechas dentro del ciclo financiero actual."""
    imprimir_titulo("CARGAR DATOS DEMO ACTUALIZADOS")
    print("Esta opcion reemplazara los datos actuales por informacion de ejemplo.")
    print("Sirve para que el dashboard tenga gastos visibles en el ciclo actual.")
    print()

    confirmar = leer_si_no("Confirmas cargar datos demo y sobrescribir el JSON actual? (s/n): ")

    if confirmar == "n":
        print("[OK] No se modificaron los datos.")
        pausar()
        return None

    hoy = datetime.date.today()
    dia_corte = 1
    inicio_ciclo, fin_ciclo = obtener_ciclo_actual(dia_corte)
    dias_transcurridos = (hoy - inicio_ciclo).days

    fecha_hoy = formatear_fecha(hoy)
    fecha_inicio = formatear_fecha(inicio_ciclo)

    if dias_transcurridos >= 2:
        fecha_reciente = formatear_fecha(hoy - datetime.timedelta(days=2))
    else:
        fecha_reciente = fecha_hoy

    if dias_transcurridos >= 5:
        fecha_intermedia = formatear_fecha(hoy - datetime.timedelta(days=5))
    else:
        fecha_intermedia = fecha_inicio

    datos_demo = {
        "configuracion": {
            "presupuesto_global": 5000.0,
            "dia_corte": dia_corte
        },
        "categorias": crear_copia_categorias_base(),
        "gastos": []
    }

    gastos_demo = [
        Gasto(1, 125.50, "Comida", "Supermercado semanal", fecha_hoy),
        Gasto(2, 80.00, "Transporte", "Gasolina", fecha_reciente),
        Gasto(3, 210.75, "Salud", "Medicina", fecha_intermedia),
        Gasto(4, 150.00, "Educación", "Materiales de clase", fecha_hoy),
        Gasto(5, 95.25, "Familia", "Regalo familiar", fecha_inicio),
        Gasto(6, 60.00, "Ocio personal", "Cine", fecha_reciente)
    ]

    for gasto in gastos_demo:
        datos_demo["gastos"].append(gasto.convertir_a_diccionario())

    datos_demo = asegurar_estructura(datos_demo)
    guardar_datos(datos_demo)
    print("[OK] Datos demo actualizados guardados en " + ARCHIVO_DATOS + ".")
    print("Ciclo demo: " + formatear_fecha(inicio_ciclo) + " al " + formatear_fecha(fin_ciclo))
    print("Gastos demo cargados: " + str(len(datos_demo["gastos"])))
    pausar()
    return datos_demo


def construir_barra_progreso(porcentaje):
    try:
        porcentaje_visual = float(porcentaje)

        if porcentaje_visual < 0:
            porcentaje_visual = 0

        if porcentaje_visual > 100:
            porcentaje_visual = 100

        bloques_llenos = int(porcentaje_visual / 10)

        if bloques_llenos > ANCHO_BARRA:
            bloques_llenos = ANCHO_BARRA

        bloques_vacios = ANCHO_BARRA - bloques_llenos
        barra = "[" + ("█" * bloques_llenos) + ("░" * bloques_vacios) + "]"
        return barra
    except Exception:
        return "[" + ("░" * ANCHO_BARRA) + "]"


def mostrar_dashboard(datos):
    imprimir_titulo("ASISTENTE INTELIGENTE DE FINANZAS Y PRESUPUESTOS")

    try:
        dia_corte = datos["configuracion"]["dia_corte"]
        presupuesto_global = float(datos["configuracion"]["presupuesto_global"])
        inicio_ciclo, fin_ciclo = obtener_ciclo_actual(dia_corte)
        gastos_ciclo = obtener_gastos_del_ciclo(datos)
        total_gastado = calcular_total_gastado(gastos_ciclo)
        gastos_por_categoria = calcular_gastos_por_categoria(datos, gastos_ciclo)

        # Matematica del dashboard global:
        # porcentaje_global = gasto del ciclo / presupuesto global * 100.
        # La barra visual se limita a 100%, pero el numero puede pasar de 100%
        # para mostrar cuando el usuario ya excedio su presupuesto.
        if presupuesto_global <= 0:
            porcentaje_global = 0.0
        else:
            porcentaje_global = (total_gastado / presupuesto_global) * 100

        print("Ciclo actual: " + formatear_fecha(inicio_ciclo) + " al " + formatear_fecha(fin_ciclo))
        print("Presupuesto global: " + formatear_dinero(presupuesto_global))
        print("Gastado en ciclo: " + formatear_dinero(total_gastado))
        print("Progreso global: " + construir_barra_progreso(porcentaje_global) + " " + formatear_porcentaje(porcentaje_global))
        print()
        print("Categorias activas:")

        if len(datos["categorias"]) == 0:
            print("  [!] No hay categorias registradas.")
        else:
            for categoria in datos["categorias"]:
                gasto_categoria = 0.0

                if categoria in gastos_por_categoria:
                    gasto_categoria = gastos_por_categoria[categoria]

                # Matematica por categoria:
                # porcentaje_categoria = gasto de la categoria / gasto total del ciclo * 100.
                # Si no hay gastos en el ciclo, se usa 0 para evitar division entre cero.
                if total_gastado <= 0:
                    porcentaje_categoria = 0.0
                else:
                    porcentaje_categoria = (gasto_categoria / total_gastado) * 100

                print("  - " + categoria + ": " + formatear_dinero(gasto_categoria) + " (" + formatear_porcentaje(porcentaje_categoria) + " del gasto total)")

        print()
    except Exception:
        print("[!] No se pudo calcular el dashboard, pero el programa continuara.")


def mostrar_menu_principal(datos):
    mostrar_dashboard(datos)
    print("MENU PRINCIPAL")
    print("1. Agregar Gasto")
    print("2. Editar Presupuesto")
    print("3. Editar Fechas (Dia de corte)")
    print("4. Administrar Categorias (Agregar/Eliminar)")
    print("5. Historial y Correcciones (Ver/Editar/Eliminar gastos)")
    print("6. Cargar datos demo actualizados")
    print("7. Salir")
    print()

    return leer_entero("Elige una opcion (1-7): ", 1, 7)


def mostrar_categorias_numeradas(datos):
    print("Categorias disponibles:")

    contador = 1
    for categoria in datos["categorias"]:
        print("  " + str(contador) + ". " + categoria)
        contador = contador + 1


def seleccionar_categoria(datos):
    while True:
        try:
            mostrar_categorias_numeradas(datos)

            if len(datos["categorias"]) == 0:
                print("[!] No hay categorias. Agrega una categoria primero.")
                return ""

            opcion = leer_entero("Elige una categoria por numero: ", 1, len(datos["categorias"]))
            return datos["categorias"][opcion - 1]
        except Exception:
            print("[!] No se pudo seleccionar la categoria. Intenta de nuevo.")


def obtener_siguiente_id(datos):
    mayor = 0

    try:
        for gasto in datos["gastos"]:
            numero = obtener_numero_desde_id(gasto.get("id", 0))

            if numero > mayor:
                mayor = numero
    except Exception:
        mayor = 0

    return mayor + 1


def agregar_gasto(datos):
    while True:
        imprimir_titulo("AGREGAR GASTO")

        monto = leer_float("Monto Q: ", 0.01)
        categoria = seleccionar_categoria(datos)

        if categoria == "":
            return

        descripcion = leer_texto("Descripcion (opcional, ENTER para omitir): ", permitir_vacio=True)
        fecha = leer_fecha_opcional("Fecha DD/MM/AAAA (opcional, ENTER para usar hoy): ")

        gasto = Gasto(obtener_siguiente_id(datos), monto, categoria, descripcion, fecha)
        nuevo_gasto = gasto.convertir_a_diccionario()

        datos["gastos"].append(nuevo_gasto)
        guardar_datos(datos)

        print("[OK] Gasto agregado.")
        print(gasto.resumen())

        respuesta = leer_si_no("¿Deseas agregar otro gasto? (s/n): ")

        if respuesta == "n":
            pausar()
            return


def editar_presupuesto(datos):
    imprimir_titulo("EDITAR PRESUPUESTO")

    try:
        presupuesto_actual = datos["configuracion"]["presupuesto_global"]
        print("Presupuesto actual: " + formatear_dinero(presupuesto_actual))
    except Exception:
        print("Presupuesto actual: Q0.00")

    nuevo_presupuesto = leer_float("Nuevo presupuesto global Q: ", 0.01)
    datos["configuracion"]["presupuesto_global"] = nuevo_presupuesto
    guardar_datos(datos)
    print("[OK] Presupuesto actualizado.")
    pausar()


def editar_fechas(datos):
    imprimir_titulo("EDITAR FECHAS")

    try:
        dia_actual = datos["configuracion"]["dia_corte"]
        inicio_ciclo, fin_ciclo = obtener_ciclo_actual(dia_actual)

        print("Dia de corte actual: " + str(dia_actual))
        print("Con este dia de corte, el ciclo presente va de " + formatear_fecha(inicio_ciclo) + " a " + formatear_fecha(fin_ciclo) + ".")
        print("El dia de corte debe estar entre 1 y 28 para que exista en todos los meses.")
    except Exception:
        print("[!] No se pudo leer el ciclo actual.")

    nuevo_dia = leer_entero("Nuevo dia de corte mensual (1-28): ", 1, 28)
    datos["configuracion"]["dia_corte"] = nuevo_dia
    guardar_datos(datos)

    inicio_nuevo, fin_nuevo = obtener_ciclo_actual(nuevo_dia)
    print("[OK] Dia de corte actualizado.")
    print("Nuevo ciclo presente: " + formatear_fecha(inicio_nuevo) + " a " + formatear_fecha(fin_nuevo) + ".")
    pausar()


def agregar_nueva_categoria(datos):
    imprimir_titulo("AGREGAR NUEVA CATEGORIA")
    mostrar_categorias_numeradas(datos)
    print()

    nueva_categoria = leer_texto("Nombre de la nueva categoria: ")

    if categoria_existe(datos, nueva_categoria):
        print("[!] Esa categoria ya existe. No se agrego duplicada.")
        pausar()
        return

    datos["categorias"].append(nueva_categoria.strip())
    guardar_datos(datos)
    print("[OK] Categoria agregada.")
    pausar()


def categoria_usada_recursivamente(gastos, categoria_busqueda, indice=0):
    """Busca recursivamente si una categoria ya aparece en los gastos."""
    try:
        if indice >= len(gastos):
            return False

        categoria_normalizada = str(categoria_busqueda).strip().lower()
        gasto_actual = gastos[indice]

        if isinstance(gasto_actual, dict):
            categoria_gasto = str(gasto_actual.get("categoria", "")).strip().lower()

            if categoria_gasto == categoria_normalizada:
                return True

            if "categorias" in gasto_actual:
                categorias_gasto = gasto_actual["categorias"]

                if isinstance(categorias_gasto, list):
                    for categoria_antigua in categorias_gasto:
                        if str(categoria_antigua).strip().lower() == categoria_normalizada:
                            return True

        return categoria_usada_recursivamente(gastos, categoria_busqueda, indice + 1)
    except Exception:
        return False


def eliminar_categoria(datos):
    """Elimina una categoria solo si no ha sido usada en el historial."""
    imprimir_titulo("ELIMINAR CATEGORIA")
    mostrar_categorias_numeradas(datos)
    print()

    if len(datos["categorias"]) == 0:
        print("[!] No hay categorias registradas para eliminar.")
        pausar()
        return

    opcion = leer_entero("Elige la categoria a eliminar por numero: ", 1, len(datos["categorias"]))
    categoria_eliminar = datos["categorias"][opcion - 1]
    categoria_busqueda = categoria_eliminar.strip().lower()

    tiene_gastos = categoria_usada_recursivamente(datos["gastos"], categoria_busqueda)

    if tiene_gastos:
        print("[!] No se puede eliminar porque ya tiene gastos registrados en el historial.")
        pausar()
        return

    nuevas_categorias = []

    for categoria in datos["categorias"]:
        if categoria.strip().lower() != categoria_busqueda:
            nuevas_categorias.append(categoria)

    datos["categorias"] = nuevas_categorias
    guardar_datos(datos)
    print("[OK] Categoria eliminada.")
    pausar()


def editar_categorias(datos):
    while True:
        imprimir_titulo("ADMINISTRAR CATEGORIAS")
        mostrar_categorias_numeradas(datos)
        print()
        print("1. Agregar nueva categoria")
        print("2. Eliminar categoria")
        print("3. Volver al menu principal")
        print()

        opcion = leer_entero("Elige una opcion (1-3): ", 1, 3)

        if opcion == 1:
            agregar_nueva_categoria(datos)
        elif opcion == 2:
            eliminar_categoria(datos)
        else:
            return


def imprimir_gasto(gasto):
    try:
        descripcion = gasto["descripcion"]

        if descripcion == "":
            descripcion = "(sin descripcion)"

        texto = "ID " + str(gasto["id"])
        texto = texto + " | " + str(gasto["fecha"])
        texto = texto + " | " + str(gasto["categoria"])
        texto = texto + " | " + formatear_dinero(gasto["monto"])
        texto = texto + " | " + descripcion
        print(texto)
    except Exception:
        print("[!] Gasto con datos incompletos.")


def mostrar_historial_ciclo(datos):
    gastos_ciclo = obtener_gastos_del_ciclo(datos)

    try:
        inicio_ciclo, fin_ciclo = obtener_ciclo_actual(datos["configuracion"]["dia_corte"])
        print("Gastos del ciclo " + formatear_fecha(inicio_ciclo) + " al " + formatear_fecha(fin_ciclo) + ":")
    except Exception:
        print("Gastos del ciclo actual:")

    if len(gastos_ciclo) == 0:
        print("  No hay gastos registrados en el ciclo actual.")
        return gastos_ciclo

    for gasto in gastos_ciclo:
        imprimir_gasto(gasto)

    total = calcular_total_gastado(gastos_ciclo)
    print("Total del ciclo: " + formatear_dinero(total))
    return gastos_ciclo


def buscar_gasto_por_id(gastos, id_buscado):
    for gasto in gastos:
        try:
            if obtener_numero_desde_id(gasto["id"]) == id_buscado:
                return gasto
        except Exception:
            pass

    return None


def eliminar_gasto_por_id(datos, id_buscado):
    nuevos_gastos = []
    eliminado = False

    for gasto in datos["gastos"]:
        try:
            if obtener_numero_desde_id(gasto["id"]) == id_buscado:
                eliminado = True
            else:
                nuevos_gastos.append(gasto)
        except Exception:
            nuevos_gastos.append(gasto)

    datos["gastos"] = nuevos_gastos
    return eliminado


def historial_y_correcciones(datos):
    while True:
        imprimir_titulo("HISTORIAL Y CORRECCIONES")
        gastos_ciclo = mostrar_historial_ciclo(datos)

        if len(gastos_ciclo) == 0:
            print()
            print("1. Volver al menu principal")
            leer_entero("Elige 1 para volver: ", 1, 1)
            return

        print()
        print("Escribe el ID de un gasto para corregirlo.")
        print("Escribe 0 para volver al menu principal.")
        id_buscado = leer_entero("ID: ", 0, None)

        if id_buscado == 0:
            return

        gasto = buscar_gasto_por_id(gastos_ciclo, id_buscado)

        if gasto is None:
            print("[!] No se encontro ese ID dentro del ciclo actual.")
            continue

        imprimir_titulo("GASTO SELECCIONADO")
        imprimir_gasto(gasto)
        print()
        print("1. Modificar monto")
        print("2. Eliminar gasto")
        print("3. Volver al historial")

        opcion = leer_entero("Elige una opcion (1-3): ", 1, 3)

        if opcion == 1:
            nuevo_monto = leer_float("Nuevo monto Q: ", 0.01)
            gasto["monto"] = nuevo_monto
            guardar_datos(datos)
            print("[OK] Monto actualizado. El dashboard se recalculara automaticamente.")
            pausar()
        elif opcion == 2:
            confirmar = leer_si_no("Confirmas eliminar este gasto? (s/n): ")

            if confirmar == "s":
                eliminado = eliminar_gasto_por_id(datos, id_buscado)

                if eliminado:
                    guardar_datos(datos)
                    print("[OK] Gasto eliminado. El dashboard se recalculara automaticamente.")
                    pausar()
                else:
                    print("[!] No se pudo eliminar el gasto.")
                    pausar()
        else:
            continue


def ejecutar_aplicacion():
    """Inicia la aplicacion de consola y controla el menu principal."""
    datos = cargar_datos()

    if datos is None:
        datos = onboarding_dia_cero()

    while True:
        try:
            opcion = mostrar_menu_principal(datos)

            if opcion == 1:
                agregar_gasto(datos)
            elif opcion == 2:
                editar_presupuesto(datos)
            elif opcion == 3:
                editar_fechas(datos)
            elif opcion == 4:
                editar_categorias(datos)
            elif opcion == 5:
                historial_y_correcciones(datos)
            elif opcion == 6:
                datos_demo = cargar_datos_demo_actualizados()

                if datos_demo is not None:
                    datos = datos_demo
            elif opcion == 7:
                guardar_datos(datos)
                print("Datos guardados en " + ARCHIVO_DATOS + ". Hasta luego.")
                break
        except Exception:
            print("[!] Ocurrio un error inesperado, pero el programa continuara.")
            guardar_datos(datos)


if __name__ == "__main__":
    ejecutar_aplicacion()
