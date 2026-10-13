def es_numero(caracter: str) -> bool:
    """
    Verifica si un carácter es un dígito (0-9).

    Args:
        caracter (str): carácter a evaluar.

    Retorno:
        bool: True si es un dígito, False en caso contrario.
    """
    retorno = False
    codigo = ord(caracter)

    if codigo >= 48 and codigo <= 57:
        retorno = True

    return retorno

def es_numerico(cadena: str) -> bool:
    """
    Verifica que una cadena no esté vacía y contenga solo dígitos.

    Args:
        cadena (str): texto a evaluar.

    Retorno:
        bool: True si la cadena es numérica, False en caso contrario.
    """
    retorno = cadena != ""

    for caracter in cadena:
        if es_numero(caracter) == False:
            retorno = False
            break

    return retorno

def es_letra(caracter: str) -> bool:
    """
    Verifica si un carácter es una letra (mayúscula o minúscula),
    incluyendo vocales acentuadas, ñ y ü.

    Args:
        caracter (str): carácter a evaluar.

    Retorno:
        bool: True si es una letra, False en caso contrario.
    """
    retorno = False
    codigo = ord(caracter)

    if (codigo >= 65 and codigo <= 90) or \
        (codigo >= 97 and codigo <= 122) or \
        codigo == 193 or codigo == 201 or codigo == 205 or \
        codigo == 211 or codigo == 218 or codigo == 220 or \
        codigo == 225 or codigo == 233 or codigo == 237 or \
        codigo == 243 or codigo == 250 or codigo == 252 or \
        codigo == 209 or codigo == 241:
        retorno = True

    return retorno

def es_alfabetico(cadena: str) -> bool:
    """
    Verifica que una cadena contenga solo letras y espacios,
    y que tenga al menos una letra.

    Args:
        cadena (str): texto a evaluar.

    Retorno:
        bool: True si es alfabética, False en caso contrario.
    """
    retorno = True
    hay_letra = False

    for caracter in cadena:
        if es_letra(caracter):
            hay_letra = True
        elif ord(caracter) != 32:
            retorno = False
            break

    if hay_letra == False:
        retorno = False

    return retorno

def es_genero(genero: str) -> bool:
    """
    Verifica que el género sea F, M o X (se aceptan también minúsculas).

    Args:
        genero (str): género a evaluar.

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = False

    if genero == "F" or genero == "M" or genero == "X" or \
        genero == "f" or genero == "m" or genero == "x":
        retorno = True

    return retorno

def es_nota(nota: str) -> bool:
    """
    Verifica que una nota sea un entero entre 1 y 10.

    Args:
        nota (str): nota ingresada como texto.

    Retorno:
        bool: True si es un entero entre 1 y 10, False en caso contrario.
    """
    retorno = False

    if es_numerico(nota):
        valor = int(nota)
        if valor >= 1 and valor <= 10:
            retorno = True

    return retorno

def cargar_legajo() -> int:
    """
    Pide un legajo por consola y lo valida hasta que sea numérico.

    Retorno:
        int: legajo ingresado.
    """
    legajo = input("Ingrese el legajo: ")

    while es_numerico(legajo) == False:
        print("Error. Ingrese un legajo numérico.")
        legajo = input("Ingrese el legajo: ")

    return int(legajo)

def cargar_apellido_nombre() -> str:
    """
    Pide el apellido y nombre por consola y lo valida hasta que
    contenga solo letras y espacios.

    Retorno:
        str: apellido y nombre ingresados.
    """
    nombre = input("Ingrese apellido y nombre: ")

    while es_alfabetico(nombre) == False:
        print("Error. Ingrese solamente letras y espacios.")
        nombre = input("Ingrese apellido y nombre: ")

    return nombre

def cargar_genero() -> str:
    """
    Pide el género por consola y lo valida hasta que sea F, M o X.
    Si se ingresa en minúscula, lo devuelve en mayúscula.

    Retorno:
        str: género ("F", "M" o "X").
    """
    genero = input("Ingrese el género (F/M/X): ")

    while es_genero(genero) == False:
        print("Error. Ingrese F, M o X.")
        genero = input("Ingrese el género (F/M/X): ")

    if genero == "f":
        genero = "F"
    elif genero == "m":
        genero = "M"
    elif genero == "x":
        genero = "X"

    return genero

def cargar_nota(parcial: str) -> int:
    """
    Pide una nota por consola y la valida hasta que sea un entero
    entre 1 y 10.

    Args:
        parcial (str): nombre del parcial ("Primer" o "Segundo"), se usa solo en el mensaje.

    Retorno:
        int: nota ingresada.
    """
    nota = input(f"Ingrese la nota del {parcial} parcial (1-10): ")

    while es_nota(nota) == False:
        print("Error. Ingrese un entero entre 1 y 10.")
        nota = input(f"Ingrese la nota del {parcial} parcial (1-10): ")

    return int(nota)

def cargar_estudiantes(legajos: list,
                        apellidos_nombres: list,
                        generos: list,
                        notas_primer_parcial: list,
                        notas_segundo_parcial: list) -> None:
    """
    Carga los datos de todos los estudiantes en las listas paralelas.
    La cantidad de estudiantes es el tamaño de las listas.

    Args:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        notas_primer_parcial (list): notas del primer parcial.
        notas_segundo_parcial (list): notas del segundo parcial.

    Retorno:
        None: modifica las listas originales.
    """
    for i in range(len(legajos)):
        print(f"\nEstudiante {i + 1}")

        legajos[i] = cargar_legajo()
        apellidos_nombres[i] = cargar_apellido_nombre()
        generos[i] = cargar_genero()
        notas_primer_parcial[i] = cargar_nota("Primer")
        notas_segundo_parcial[i] = cargar_nota("Segundo")

    print("\nDatos cargados correctamente.")

def mostrar_estudiante(legajos: list,
                        apellidos_nombres: list,
                        generos: list,
                        notas_primer_parcial: list,
                        notas_segundo_parcial: list,
                        indice: int,
                        promedios: list = None) -> None:
    """
    Muestra los datos de un único estudiante.

    Args:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        notas_primer_parcial (list): notas del primer parcial.
        notas_segundo_parcial (list): notas del segundo parcial.
        indice (int): posición del estudiante a mostrar.
        promedios (list): promedios (opcional). Si se pasa y ya
        tiene el valor de esa posición, se muestra.

    Retorno:
        None.
    """
    print(f"Legajo: {legajos[indice]}")
    print(f"Apellido y nombre: {apellidos_nombres[indice]}")
    print(f"Género: {generos[indice]}")
    print(f"Primer parcial: {notas_primer_parcial[indice]}")
    print(f"Segundo parcial: {notas_segundo_parcial[indice]}")

    if promedios is not None and len(promedios) > indice:
        print(f"Promedio: {promedios[indice]:.2f}")

    print("-" * 40)

def mostrar_estudiantes(legajos: list,
                        apellidos_nombres: list,
                        generos: list,
                        notas_primer_parcial: list,
                        notas_segundo_parcial: list,
                        promedios: list = None,
                        criterio: str = "TODOS",
                        valor=None) -> None:
    """
    Recorre las listas y muestra un informe con título y los
    estudiantes que cumplan el criterio. Para cada uno llama a
    mostrar_estudiante.

    Args:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        notas_primer_parcial (list): notas del primer parcial.
        notas_segundo_parcial (list): notas del segundo parcial.
        promedios (list): promedios (opcional, necesario si el criterio es "MAYOR").
        criterio (str): "TODOS" (muestra todos), "MAYOR" (solo los que tienen promedio igual a valor) o
        "LEGAJO" (solo los que tienen legajo igual a valor).
        valor: promedio o legajo a comparar según el criterio.

    Retorno:
        None.
    """
    if criterio == "MAYOR":
        print("\n========== ESTUDIANTE/S CON MAYOR PROMEDIO ==========")
    elif criterio == "LEGAJO":
        print("\n========== ESTUDIANTE ENCONTRADO ==========")
    else:
        print("\n========== INFORME DE ESTUDIANTES ==========")

    for i in range(len(legajos)):
        if criterio == "TODOS" or \
            (criterio == "MAYOR" and promedios[i] == valor) or \
            (criterio == "LEGAJO" and legajos[i] == valor):
            mostrar_estudiante(
                legajos,
                apellidos_nombres,
                generos,
                notas_primer_parcial,
                notas_segundo_parcial,
                i,
                promedios
            )

def mostrar_promedios(apellidos_nombres: list, promedios: list) -> None:
    """
    Muestra el promedio de cada estudiante junto a su nombre.

    Args:
        apellidos_nombres (list): lista de apellidos y nombres.
        promedios (list): promedios de los estudiantes.

    Retorno:
        None.
    """
    for i in range(len(promedios)):
        print(f"{apellidos_nombres[i]} - Promedio: {promedios[i]:.2f}")

def calcular_promedio(nota1: int, nota2: int) -> float:
    """
    Calcula el promedio de dos notas, con dos decimales.

    Args:
        nota1 (int): primera nota (1 a 10).
        nota2 (int): segunda nota (1 a 10).

    Retorno:
        float: promedio entre 1.00 y 10.00 redondeado a 2 decimales.
    """
    promedio = (nota1 + nota2) / 2
    return round(promedio, 2)

def calcular_promedios(notas_primer_parcial: list,
                        notas_segundo_parcial: list) -> list:
    """
    Calcula el promedio de cada estudiante y lo guarda en una nueva lista.

    Args:
        notas_primer_parcial (list): notas del primer parcial.
        notas_segundo_parcial (list): notas del segundo parcial.

    Retorno:
        list: lista de promedios, paralela a las demás listas.
    """
    promedios = [0.0] * len(notas_primer_parcial)

    for i in range(len(notas_primer_parcial)):
        promedios[i] = calcular_promedio(
            notas_primer_parcial[i],
            notas_segundo_parcial[i]
        )

    return promedios

def mostrar_mayor_promedio(legajos: list,
                            apellidos_nombres: list,
                            generos: list,
                            notas_primer_parcial: list,
                            notas_segundo_parcial: list,
                            promedios: list) -> None:
    """
    Busca el mayor promedio y muestra el/los estudiante/s que lo tienen
    (puede haber empates).

    Args:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        notas_primer_parcial (list): notas del primer parcial.
        notas_segundo_parcial (list): notas del segundo parcial.
        promedios (list): promedios de los estudiantes.

    Retorno:
        None.
    """
    if len(promedios) == 0:
        print("Primero debe calcular los promedios.")
    else:
        mayor = promedios[0]

        for i in range(1, len(promedios)):
            if promedios[i] > mayor:
                mayor = promedios[i]

        print(f"\nMayor promedio: {mayor:.2f}")

        mostrar_estudiantes(
            legajos,
            apellidos_nombres,
            generos,
            notas_primer_parcial,
            notas_segundo_parcial,
            promedios,
            "MAYOR",
            mayor
        )

def intercambiar(lista: list, i: int, j: int) -> None:
    """
    Intercambia los elementos de las posiciones i y j de una lista.

    Args:
        lista (list): lista a modificar.
        i (int): primera posición.
        j (int): segunda posición.

    Retorno:
        None: modifica la lista original.
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def ordenar_por_promedio(legajos: list,
                        apellidos_nombres: list,
                        generos: list,
                        notas_primer_parcial: list,
                        notas_segundo_parcial: list,
                        promedios: list,
                        orden: str) -> None:
    """
    Ordena todas las listas paralelas según el promedio.

    Args:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        notas_primer_parcial (list): notas del primer parcial.
        notas_segundo_parcial (list): notas del segundo parcial.
        promedios (list): promedios de los estudiantes.
        orden (str): "ASC" (ascendente) o "DESC" (descendente).

    Retorno:
        None: modifica las listas originales. Si el orden no es
        válido, informa el error y no modifica nada.
    """
    if orden != "ASC" and orden != "DESC":
        print('Error. El orden debe ser "ASC" o "DESC".')
    else:
        n = len(promedios)
                                #[9,8,5,2,10]1.4,
        for i in range(n - 1):
            for j in range(i + 1, n):

                if (orden == "DESC" and promedios[j] > promedios[i]) or \
                    (orden == "ASC" and promedios[j] < promedios[i]):

                    intercambiar(promedios, i, j)
                    intercambiar(legajos, i, j)
                    intercambiar(apellidos_nombres, i, j)
                    intercambiar(generos, i, j)
                    intercambiar(notas_primer_parcial, i, j)
                    intercambiar(notas_segundo_parcial, i, j)

def buscar_estudiante(legajos: list,
                    apellidos_nombres: list,
                    generos: list,
                    notas_primer_parcial: list,
                    notas_segundo_parcial: list,
                    legajo_buscar: int,
                    promedios: list = None) -> None:
    """
    Busca un estudiante por legajo y muestra sus datos usando
    mostrar_estudiantes. Si no existe, informa que no se encontró.

    Args:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        notas_primer_parcial (list): notas del primer parcial.
        notas_segundo_parcial (list): notas del segundo parcial.
        legajo_buscar (int): legajo que se desea buscar.
        promedios (list): promedios (opcional). Si ya fueron
                        calculados, se muestran junto a los datos.

    Retorno:
        None.
    """
    encontrado = False

    for i in range(len(legajos)):
        if legajos[i] == legajo_buscar:
            encontrado = True
            break

    if encontrado:
        mostrar_estudiantes(
            legajos,
            apellidos_nombres,
            generos,
            notas_primer_parcial,
            notas_segundo_parcial,
            promedios,
            "LEGAJO",
            legajo_buscar
        )
    else:
        print("No se encontró un estudiante con ese legajo.")
