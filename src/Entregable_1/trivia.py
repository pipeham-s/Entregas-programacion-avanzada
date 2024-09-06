import itertools
import csv
import os
import random
from functools import reduce


def leer_archivo_csv_generador(ruta_archivo):
    """ Lee un archivo CSV y devuelve un generador de líneas. """
    # Para evitar problemas en la ruta al cargar el archivo
    ruta_archivo = os.path.join(
        os.path.dirname(__file__), 'trivia_questions.csv')
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Se omite el encabezado
        for linea in lector:
            yield linea


def seleccionar_preguntas_aleatorias_generador(lineas, num_preguntas=5):
    """ Selecciona preguntas aleatoriamente del generador y las guarda en listas separadas. """
    preguntas = list(
        lineas)  # Convertir el generador a lista para permitir el muestreo
    # Extrae n preguntas aleatoriamente
    seleccionadas = random.sample(preguntas, num_preguntas)
    # Crea una lista para cada pregunta
    listas_de_preguntas = [[pregunta] for pregunta in seleccionadas]
    return listas_de_preguntas


def procesar_lineas(lineas):
    """ Procesa las líneas del archivo CSV y convierte a cada una en un diccionario. """
    return list(map(lambda linea: {
        'pregunta': linea[0],
        'opcion_1': linea[1],
        'opcion_2': linea[2],
        'opcion_3': linea[3],
        'respuesta_correcta': linea[4]
    }, lineas))


def procesar_preguntas_combinadas(listas_de_preguntas):
    """ Combina las listas de preguntas y las procesa. """
    # Uso de itertools.chain para aplanar la lista de listas
    preguntas_combinadas = list(
        itertools.chain.from_iterable(listas_de_preguntas))
    preguntas_procesadas = procesar_lineas(preguntas_combinadas)
    return preguntas_procesadas


def leer_y_procesar_csv(ruta_archivo):
    """ Lee el archivo CSV, genera las preguntas, las selecciona aleatoriamente y las procesa. """
    lineas_generador = leer_archivo_csv_generador(ruta_archivo)
    lineas_aleatorias = seleccionar_preguntas_aleatorias_generador(
        lineas_generador)
    preguntas_procesadas = procesar_preguntas_combinadas(lineas_aleatorias)
    return preguntas_procesadas


def print_colored(text, color):
    """ Imprime el texto con el color especificado. """
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "end": "\033[0m",
    }
    print(colors[color] + text + colors["end"])


def validate_input(func):
    """ Decorador para validar que la entrada sean números. """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print_colored("Por favor ingresa solo números.", "red")
            return func(*args, **kwargs)
    return wrapper


@validate_input
def obtener_respuesta(pregunta):
    """ Obtiene la respuesta del usuario y verifica si es correcta. """
    print_colored(f"\nPregunta: {pregunta['pregunta']}", "cyan")
    print(f"1: {pregunta['opcion_1']}")
    print(f"2: {pregunta['opcion_2']}")
    print(f"3: {pregunta['opcion_3']}")
    respuesta = int(input("Ingresa el número de tu respuesta: "))
    if respuesta not in [1, 2, 3]:
        print_colored("Respuesta inválida. Inténtalo de nuevo.", "red")
        return obtener_respuesta(pregunta)
    if pregunta[f'opcion_{respuesta}'] == pregunta['respuesta_correcta']:
        print_colored("\n¡Correcto!", "green")
        return 10
    else:
        print_colored(f"\nIncorrecto. La respuesta correcta era: {pregunta['respuesta_correcta']}", "red")
        return 0


def mostrar_banner_gracias():
    """ Muestra un banner de agradecimiento. """
    print(r"""
        
 ██████╗ ██████╗  █████╗  ██████╗██╗ █████╗ ███████╗    ██████╗  ██████╗ ██████╗          ██╗██╗   ██╗ ██████╗  █████╗ ██████╗ ██╗    
██╔════╝ ██╔══██╗██╔══██╗██╔════╝██║██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗██╔══██╗         ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██║    
██║  ███╗██████╔╝███████║██║     ██║███████║███████╗    ██████╔╝██║   ██║██████╔╝         ██║██║   ██║██║  ███╗███████║██████╔╝██║    
██║   ██║██╔══██╗██╔══██║██║     ██║██╔══██║╚════██║    ██╔═══╝ ██║   ██║██╔══██╗    ██   ██║██║   ██║██║   ██║██╔══██║██╔══██╗╚═╝    
╚██████╔╝██║  ██║██║  ██║╚██████╗██║██║  ██║███████║    ██║     ╚██████╔╝██║  ██║    ╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██║  ██║██╗    
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝     ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝    
                                                                                                                                      
          
          """)


def mostrar_divisor():
    """ Muestra una línea divisoria. """
    print("\n" + "-" * 50 + "\n")  # Imprime una línea divisoria


@validate_input
def jugar_otra_vez():
    """ Pregunta al usuario si desea jugar otra vez. """
    respuesta = input("¿Deseas jugar otra vez? (s/n): ")
    if respuesta.lower() == 's':
        mostrar_divisor()

        jugar()  # Vuelve a jugar
    elif respuesta.lower() == 'n':
        mostrar_banner_gracias()
    else:
        print("Respuesta no reconocida.")
        jugar_otra_vez()


def jugar_recursivo(preguntas: list[dict[str, str]], resultados: list[int], indice: int = 0):
    """ Juega el trivial de forma recursiva. """
    if indice == 0:
        resultados = []
    if indice < len(preguntas):
        puntos = obtener_respuesta(preguntas[indice])
        resultados.append(puntos)
        return jugar_recursivo(preguntas, resultados, indice + 1)
    else:
        total_puntos = reduce(lambda x, y: x + y, resultados)
        print(f"\nTu puntuación final es: {total_puntos} puntos.")
        return total_puntos


def jugar():
    """ Inicia el juego del trivial. """
    preguntas = leer_y_procesar_csv('trivia_questions.csv')
    jugar_recursivo(preguntas, resultados=[])
    jugar_otra_vez()


def mostrar_bienvenida():
    """ Muestra un banner de bienvenida. """
    print_colored(r"""
                                                                   
 ████████╗██████╗ ██╗██╗   ██╗██╗ █████╗ ██╗     
╚══██╔══╝██╔══██╗██║██║   ██║██║██╔══██╗██║     
   ██║   ██████╔╝██║██║   ██║██║███████║██║     
   ██║   ██╔══██╗██║╚██╗ ██╔╝██║██╔══██║██║     
   ██║   ██║  ██║██║ ╚████╔╝ ██║██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                                      
    """, "cyan")
    print("¡Bienvenido al Trivial!")
    print("El Trivial es un juego de preguntas y respuestas.")
    print("Debes seleccionar la opción correcta (número del 1 al 3) para cada pregunta.")
    print("Presiona ENTER para continuar.")
    input()


def main():
    """ Función principal del programa. """
    mostrar_bienvenida()
    jugar()


if __name__ == '__main__':
    main()
