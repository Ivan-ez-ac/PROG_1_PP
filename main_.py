from funciones import *

CANTIDAD = 3

legajos = [0] * CANTIDAD
apellidos_nombres = [""] * CANTIDAD
generos = [""] * CANTIDAD
notas_primer_parcial = [0] * CANTIDAD
notas_segundo_parcial = [0] * CANTIDAD


def mostrar_menu() -> None:
    """
    Muestra por consola las opciones del menú principal.
    """
    print("\n--- MENU DE ESTUDIANTES ---")
    print("1. Cargar datos")
    print("2. Mostrar todos los estudiantes")
    print("3. Calcular promedios")
    print("4. Mostrar estudiantes ordenados por promedio (DESC)")
    print("5. Mostrar estudiante/s con mayor promedio")
    print("6. Buscar estudiante por legajo")
    print("7. Salir")


def opcion_calcular_promedios(apellidos_nombres: list,
                            notas_primer_parcial: list,
                            notas_segundo_parcial: list) -> list:
    """
    Ítem 3 del menú: calcula el promedio de cada estudiante,
    lo guarda en una nueva lista y lo muestra.

    Args:
        apellidos_nombres (list): lista de apellidos y nombres.
        notas_primer_parcial (list): notas del primer parcial.
        notas_segundo_parcial (list): notas del segundo parcial.

    Retorno:
        list: lista de promedios (paralela al resto de las listas).
    """
    promedios = calcular_promedios(
        notas_primer_parcial,
        notas_segundo_parcial
    )

    print("\n--- PROMEDIOS DE LOS ESTUDIANTES ---")
    mostrar_promedios(apellidos_nombres, promedios)

    return promedios


def opcion_mostrar_ordenados(legajos: list,
                            apellidos_nombres: list,
                            generos: list,
                            notas_primer_parcial: list,
                            notas_segundo_parcial: list,
                            promedios: list) -> None:
    """
    Ítem 4 del menú: ordena a los estudiantes por promedio de manera
    descendente y muestra el informe.

    Args:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        notas_primer_parcial (list): notas del primer parcial.
        notas_segundo_parcial (list): notas del segundo parcial.
        promedios (list): promedios de los estudiantes.

    Retorno:
        None: modifica las listas originales (quedan ordenadas).
    """
    ordenar_por_promedio(
        legajos,
        apellidos_nombres,
        generos,
        notas_primer_parcial,
        notas_segundo_parcial,
        promedios,
        "DESC"
    )

    mostrar_estudiantes(
        legajos,
        apellidos_nombres,
        generos,
        notas_primer_parcial,
        notas_segundo_parcial,
        promedios
    )

def opcion_buscar_estudiante(legajos: list,
                            apellidos_nombres: list,
                            generos: list,
                            notas_primer_parcial: list,
                            notas_segundo_parcial: list,
                            promedios: list) -> None:
    """
    Ítem 6 del menú: pide un legajo y muestra los datos del estudiante
    (con su promedio si ya fue calculado).

    Args:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        notas_primer_parcial (list): notas del primer parcial.
        notas_segundo_parcial (list): notas del segundo parcial.
        promedios (list): promedios de los estudiantes (vacía si
        todavía no se calcularon).

    Retorno:
        None.
    """
    legajo_buscar = cargar_legajo()

    buscar_estudiante(
        legajos,
        apellidos_nombres,
        generos,
        notas_primer_parcial,
        notas_segundo_parcial,
        legajo_buscar,
        promedios
    )


def opcion_salir() -> None:
    """
    Ítem 7 del menú: informa que el programa finaliza.
    """
    print("Saliendo del programa...")


def menu() -> None:
    """
    Controla el flujo del programa: muestra el menú, valida que se
    hayan cargado los datos (y calculado los promedios cuando
    corresponde) y llama a la función de cada ítem.
    """
    opcion = ""
    datos_cargados = False
    promedios_calculados = False
    promedios = []

    while opcion != "7":
        mostrar_menu()
        opcion = input("Ingrese una opcion: ")

        if opcion in ["2", "3", "4", "5", "6"] and datos_cargados == False:
            print("Primero debe cargar los datos.")

        elif opcion in ["4", "5"] and promedios_calculados == False:
            print("Primero debe calcular los promedios.")

        else:
            match opcion:

                case "1":
                    cargar_estudiantes(
                    legajos,
                    apellidos_nombres,
                    generos,
                    notas_primer_parcial,
                    notas_segundo_parcial
                )
                    datos_cargados = True
                    promedios_calculados = False
                    promedios = []

                case "2":
                    mostrar_estudiantes(
                        legajos,
                        apellidos_nombres,
                        generos,
                        notas_primer_parcial,
                        notas_segundo_parcial
                    )

                case "3":
                    promedios = opcion_calcular_promedios(
                        apellidos_nombres,
                        notas_primer_parcial,
                        notas_segundo_parcial
                    )
                    promedios_calculados = True

                case "4":
                    opcion_mostrar_ordenados(
                        legajos,
                        apellidos_nombres,
                        generos,
                        notas_primer_parcial,
                        notas_segundo_parcial,
                        promedios
                    )

                case "5":
                    mostrar_mayor_promedio(
                        legajos,
                        apellidos_nombres,
                        generos,
                        notas_primer_parcial,
                        notas_segundo_parcial,
                        promedios
                    )

                case "6":
                    opcion_buscar_estudiante(
                        legajos,
                        apellidos_nombres,
                        generos,
                        notas_primer_parcial,
                        notas_segundo_parcial,
                        promedios
                    )

                case "7":
                    opcion_salir()

                case _:
                    print("Opcion invalida.")


menu()
