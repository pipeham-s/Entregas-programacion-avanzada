import csv


def leer_archivo_csv(ruta_archivo):
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Omitir el encabezado si es necesario
        return list(lector)


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
    preguntas_procesadas = procesar_lineas(lineas)
    return preguntas_procesadas


if __name__ == '__main__':
    preguntas = leer_y_procesar_csv('trivia_questions.csv')
    print(preguntas)
