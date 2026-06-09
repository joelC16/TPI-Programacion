import csv

ARCHIVO_CSV = "dataset-paises.csv"

CONTINENTES_VALIDOS = [
    "América",
    "Europa",
    "Asia",
    "África",
    "Oceanía"
]


# =========================
# CARGA Y GUARDADO CSV
# =========================


# Convierte los datos del CSV en una lista de diccionarios
# O sea, cada fila del CSV es un diccionario de la lista
# EJ: [{"nombre": "Argentina", "poblacion": 45376763, "superficie": 2780400, "continente": "América"}]
def cargar_csv(nombre_archivo):

    paises = []

    try:

        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:

                try:

                    fila = {
                        clave.strip(): valor.strip()
                        for clave, valor in fila.items()
                    }

                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }

                    paises.append(pais)

                except (ValueError, KeyError):

                    print("Error en una fila del CSV.")

    except FileNotFoundError:

        print("No se encontró el archivo.")

    except Exception as error:

        print("Error al leer el CSV:", error)

    return paises


# Guarda la lista de países en el archivo CSV.
# Cada diccionario de la lista se convierte en una fila del archivo.
def guardar_csv(nombre_archivo, paises):

    try:

        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:

            campos = [
                "nombre",
                "poblacion",
                "superficie",
                "continente"
            ]

            escritor = csv.DictWriter(
                archivo,
                fieldnames=campos
            )

            escritor.writeheader()

            for pais in paises:

                escritor.writerow(pais)

        print("Datos guardados correctamente.")

    except Exception as error:

        print(f"Error al guardar el archivo: {error}")


# =========================
# VALIDACIONES
# =========================

# Valida que sea un número mayor a 0
def validar_entero(mensaje):

    while True:

        try:

            numero = int(input(mensaje))

            if numero > 0:
                return numero

            print("Debe ser mayor que 0.")

        except ValueError:

            print("Ingrese un número válido.")

# Valida que el texto ingresado sea correcto, no este vacio
def validar_texto(mensaje):

    while True:

        texto = input(mensaje).strip()

        if texto != "":
            return texto

        print("No puede estar vacío.")


# =========================
# UTILIDADES
# =========================

# Muestra la info del pais buscado
def mostrar_pais(pais):

    print("\n------------------")
    print(f"Nombre: {pais['nombre']}")
    print(f"Población: {pais['poblacion']}")
    print(f"Superficie: {pais['superficie']}")
    print(f"Continente: {pais['continente']}")

# Muestra una lista de los países
def mostrar_lista_paises(paises):

    if len(paises) == 0:

        print("No hay países para mostrar.")
        return

    for pais in paises:

        mostrar_pais(pais)


# =========================
# ABM
# =========================

# Se ingresa el nombre, población, superficie y continente validando si lo ingresado es valido
def agregar_pais(paises):

    nombre = validar_texto(
        "Ingrese el nombre del país: "
    )

    for pais in paises:

        if pais["nombre"].lower() == nombre.lower():

            print("Ese país ya existe.")
            return

    poblacion = validar_entero(
        "Ingrese la población: "
    )

    superficie = validar_entero(
        "Ingrese la superficie: "
    )

    while True:

        continente = validar_texto(
            "Ingrese el continente: "
        )

        if continente in CONTINENTES_VALIDOS:
            break

        print("Continente inválido. Use: América, Europa, Asia, África u Oceanía.")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    guardar_csv(ARCHIVO_CSV, paises)

    print("País agregado correctamente.")


# Se actualizan los datos de países existentes, primero se busca el país y si existe se actualiza la info
def actualizar_pais(paises):

    nombre = validar_texto(
        "Ingrese el nombre del país a actualizar: "
    )

    for pais in paises:

        if pais["nombre"].lower() == nombre.lower():

            print("\nPaís encontrado:")
            mostrar_pais(pais)

            nueva_poblacion = validar_entero(
                "Nueva población: "
            )

            nueva_superficie = validar_entero(
                "Nueva superficie: "
            )

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            guardar_csv(ARCHIVO_CSV, paises)

            print("País actualizado correctamente.")

            return

    print("No se encontró el país.")


# =========================
# BUSQUEDAS
# =========================

# Se busca país con coincidencia total o parcial. EJ: "Arg" o "entina" sirven para buscar "Argentina"
def buscar_pais(paises):

    texto = validar_texto(
        "Ingrese el nombre del país a buscar: "
    )

    encontrado = False

    for pais in paises:

        if texto.lower() in pais["nombre"].lower():

            mostrar_pais(pais)

            encontrado = True

    if not encontrado:

        print("No se encontraron países.")


# =========================
# FILTROS
# =========================

# Se filtra por continente, solamente aparecen países que son de ese continente
def filtrar_por_continente(paises):

    continente = validar_texto(
        "Ingrese el continente: "
    )

    encontrado = False

    for pais in paises:

        if pais["continente"].lower() == continente.lower():

            mostrar_pais(pais)

            encontrado = True

    if not encontrado:

        print("No se encontraron países.")

# Se filtra según la cantidad de población, se le pide al usuario dos valores para filtrar los paises según ese rango
def filtrar_por_poblacion(paises):

    minimo = validar_entero(
        "Ingrese la población mínima: "
    )

    maximo = validar_entero(
        "Ingrese la población máxima: "
    )
    
    if minimo > maximo:
        print("La población mínima no puede ser mayor que la máxima.")
        return

    cantidad = 0

    for pais in paises:

        if minimo <= pais["poblacion"] <= maximo:

            mostrar_pais(pais)

            cantidad += 1

    if cantidad == 0:

        print("No se encontraron países.")

    else:

        print(f"\nSe encontraron {cantidad} países.")

# Es la misma logica que filtrar por población pero se hace con la superficie
def filtrar_por_superficie(paises):

    minimo = validar_entero(
        "Ingrese la superficie mínima: "
    )

    maximo = validar_entero(
        "Ingrese la superficie máxima: "
    )

    if minimo > maximo:

        print(
            "La superficie mínima no puede ser mayor que la máxima."
        )

        return

    cantidad = 0

    for pais in paises:

        if minimo <= pais["superficie"] <= maximo:

            mostrar_pais(pais)

            cantidad += 1

    if cantidad == 0:

        print("No se encontraron países.")

    else:

        print(f"\nSe encontraron {cantidad} países.")


# =========================
# ORDENAMIENTOS: Aunque podríamos haber utilizado métodos como sort() y sorted decidimos usar Selection Sort para ordenar los paises según nombre/población/superficie
# =========================


# Ordena los países alfabéticamente por nombre utilizando Selection Sort.
def ordenar_por_nombre(paises):

    paises_ordenados = paises.copy()

    n = len(paises_ordenados)

    for i in range(n - 1):

        indice_minimo = i

        for j in range(i + 1, n):

            if paises_ordenados[j]["nombre"].lower() < paises_ordenados[indice_minimo]["nombre"].lower():

                indice_minimo = j

        paises_ordenados[i], paises_ordenados[indice_minimo] = (
            paises_ordenados[indice_minimo],
            paises_ordenados[i]
        )

    mostrar_lista_paises(paises_ordenados)


# Ordena los países por población utilizando Selection Sort. (misma lógica que ordenar por nombre)
def ordenar_por_poblacion(paises):

    paises_ordenados = paises.copy()

    n = len(paises_ordenados)

    for i in range(n - 1):

        indice_minimo = i

        for j in range(i + 1, n):

            if paises_ordenados[j]["poblacion"] < paises_ordenados[indice_minimo]["poblacion"]:

                indice_minimo = j

        paises_ordenados[i], paises_ordenados[indice_minimo] = (
            paises_ordenados[indice_minimo],
            paises_ordenados[i]
        )

    mostrar_lista_paises(paises_ordenados)


# Ordena los países por superficie en forma ascendente o descendente utilizando Selection Sort.
def ordenar_por_superficie(paises):

    while True:

        print("1. Ascendente")
        print("2. Descendente")

        opcion = input("Opción: ")

        if opcion in ["1", "2"]:
            break

        print("Opción inválida.")

    paises_ordenados = paises.copy()

    n = len(paises_ordenados)

    for i in range(n - 1):

        indice_minimo = i

        for j in range(i + 1, n):

            if opcion == "1":

                if paises_ordenados[j]["superficie"] < paises_ordenados[indice_minimo]["superficie"]:

                    indice_minimo = j

            else:

                if paises_ordenados[j]["superficie"] > paises_ordenados[indice_minimo]["superficie"]:

                    indice_minimo = j

        paises_ordenados[i], paises_ordenados[indice_minimo] = (
            paises_ordenados[indice_minimo],
            paises_ordenados[i]
        )

    mostrar_lista_paises(paises_ordenados)


# =========================
# ESTADISTICAS
# =========================

# Muestra el país con la mayor población.
def pais_mayor_poblacion(paises):

    if len(paises) == 0:
        print("No hay países cargados.")
        return
    mayor = paises[0] 

    for pais in paises:

        if pais["poblacion"] > mayor["poblacion"]:

            mayor = pais

    print("\nPaís con mayor población:")
    mostrar_pais(mayor)

# Muestra el país con la menor población.
def pais_menor_poblacion(paises):

    if len(paises) == 0:
        print("No hay países cargados.")
        return
    menor = paises[0]

    for pais in paises:

        if pais["poblacion"] < menor["poblacion"]:

            menor = pais

    print("\nPaís con menor población:")
    mostrar_pais(menor)

# Calcula y muestra el promedio de población.
def promedio_poblacion(paises):
    
    if len(paises) == 0:
        print("No hay países cargados.")
        return

    suma = 0

    for pais in paises:

        suma += pais["poblacion"]

    promedio = suma / len(paises)

    print(f"\nPromedio de población: {promedio:.2f}")

# Calcula y muestra el promedio de superficie.
def promedio_superficie(paises):
    
    if len(paises) == 0:
        print("No hay países cargados.")
        return

    suma = 0

    for pais in paises:

        suma += pais["superficie"]

    promedio = suma / len(paises)

    print(f"\nPromedio de superficie: {promedio:.2f}")

# Muestra la cantidad de países por continente.
def cantidad_por_continente(paises):

    continentes = {}

    for pais in paises:

        continente = pais["continente"]

        if continente in continentes:

            continentes[continente] += 1

        else:

            continentes[continente] = 1

    print()

    for continente, cantidad in continentes.items():

        print(f"{continente}: {cantidad}")


# =========================
# MENUS
# =========================

# Menú de filtros.
def menu_filtros(paises):

    while True:

        print("\n=== FILTROS ===")
        print("1. Filtrar por continente")
        print("2. Filtrar por población")
        print("3. Filtrar por superficie")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            filtrar_por_continente(paises)

        elif opcion == "2":

            filtrar_por_poblacion(paises)

        elif opcion == "3":

            filtrar_por_superficie(paises)

        elif opcion == "0":

            break

        else:

            print("Opción inválida.")

# Menú de ordenamientos.
def menu_ordenamientos(paises):

    while True:

        print("\n=== ORDENAMIENTOS ===")
        print("1. Ordenar por nombre")
        print("2. Ordenar por población")
        print("3. Ordenar por superficie")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            ordenar_por_nombre(paises)

        elif opcion == "2":

            ordenar_por_poblacion(paises)

        elif opcion == "3":

            ordenar_por_superficie(paises)

        elif opcion == "0":

            break

        else:

            print("Opción inválida.")


def menu_estadisticas(paises):

    while True:

        print("\n=== ESTADÍSTICAS ===")
        print("1. País con mayor población")
        print("2. País con menor población")
        print("3. Promedio de población")
        print("4. Promedio de superficie")
        print("5. Cantidad de países por continente")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            pais_mayor_poblacion(paises)

        elif opcion == "2":

            pais_menor_poblacion(paises)

        elif opcion == "3":

            promedio_poblacion(paises)

        elif opcion == "4":

            promedio_superficie(paises)

        elif opcion == "5":

            cantidad_por_continente(paises)

        elif opcion == "0":

            break

        else:

            print("Opción inválida.")

# Menú principal del sistema.
def menu_principal(paises):

    while True:

        print("\n=== GESTIÓN DE PAÍSES ===")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtros")
        print("5. Ordenamientos")
        print("6. Estadísticas")
        print("0. Salir")

        opcion = input("Opción: ")

        if opcion == "1":

            agregar_pais(paises)

        elif opcion == "2":

            actualizar_pais(paises)

        elif opcion == "3":

            buscar_pais(paises)

        elif opcion == "4":

            menu_filtros(paises)

        elif opcion == "5":

            menu_ordenamientos(paises)

        elif opcion == "6":

            menu_estadisticas(paises)

        elif opcion == "0":

            print("Programa finalizado.")
            break

        else:

            print("Opción inválida.")


# =========================
# MAIN
# =========================

# Función principal.
def main():

    paises = cargar_csv(ARCHIVO_CSV)

    menu_principal(paises)

main()