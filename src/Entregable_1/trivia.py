import csv
import os
import random
from functools import reduce


def leer_archivo_csv(ruta_archivo):
    # Para evitar problemas en la ruta al cargar el archivo
    ruta_archivo = os.path.join(
        os.path.dirname(__file__), 'trivia_questions.csv')
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Se omite el encabezado
        return list(lector)


def seleccionar_preguntas_aleatorias(lineas, num_preguntas=5):
    random.shuffle(lineas)
    return lineas[:num_preguntas]


def procesar_lineas(lineas):
    return list(map(lambda linea: {
        'pregunta': linea[0],
        'opcion_1': linea[1],
        'opcion_2': linea[2],
        'opcion_3': linea[3],
        'respuesta_correcta': linea[4]
    }, lineas))


def leer_y_procesar_csv(ruta_archivo):
    lineas = leer_archivo_csv(ruta_archivo)
    lineas_elejidas = seleccionar_preguntas_aleatorias(lineas)
    preguntas_procesadas = procesar_lineas(lineas_elejidas)
    return preguntas_procesadas


def obtener_respuesta(pregunta):
    print(f"\nPregunta: {pregunta['pregunta']}")
    print(f"1: {pregunta['opcion_1']}")
    print(f"2: {pregunta['opcion_2']}")
    print(f"3: {pregunta['opcion_3']}")
    respuesta = int(input("Ingresa el número de tu respuesta: "))
    if respuesta not in [1, 2, 3]:
        print("Respuesta inválida. Inténtalo de nuevo.")
        return obtener_respuesta(pregunta)
    if pregunta[f'opcion_{respuesta}'] == (pregunta['respuesta_correcta']):
        print("¡Correcto!")
        return 10
    else:
        print(
            f"Incorrecto. La respuesta correcta era: {pregunta['respuesta_correcta']}")
        return 0


def mostrar_divisor():
    print("\n" + "-" * 50 + "\n")  # Imprime una línea divisoria


def jugar_otra_vez():
    respuesta = input("¿Deseas jugar otra vez? (s/n): ")
    if respuesta.lower() == 's':
        mostrar_divisor()

        jugar()  # Suponiendo que 'main' es tu función principal
    elif respuesta.lower() == 'n':
        print("Gracias por jugar.")
    else:
        print("Respuesta no reconocida.")
        jugar_otra_vez()


def jugar_recursivo(preguntas: list[dict[str, str]], resultados: list[int], indice: int = 0):
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
    preguntas = leer_y_procesar_csv('trivia_questions.csv')
    jugar_recursivo(preguntas, resultados=[])
    jugar_otra_vez()


def mostrar_bienvenida():
    print(r"""
                                                                   
  _______ _____  _______      _______          _      
 |__   __|  __ \|_   _\ \    / /_   _|   /\   | |     
    | |  | |__) | | |  \ \  / /  | |    /  \  | |     
    | |  |  _  /  | |   \ \/ /   | |   / /\ \ | |     
    | |  | | \ \ _| |_   \  /   _| |_ / ____ \| |____ 
    |_|  |_|  \_\_____|   \/   |_____/_/    \_\______
                                                                      
    """)
    print("¡Bienvenido al Trivial!")
    print("El Trivial es un juego de preguntas y respuestas.")
    print("Debes seleccionar la opción correcta (número del 1 al 3) para cada pregunta.")
    print("Presiona ENTER para continuar.")
    input()


def main():
    mostrar_bienvenida()
    jugar()


if __name__ == '__main__':
    main()
