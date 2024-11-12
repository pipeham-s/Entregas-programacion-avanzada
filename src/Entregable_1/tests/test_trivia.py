import pytest
import os
from trivia import (
    leer_archivo_csv_generador,
    seleccionar_preguntas_aleatorias_generador,
    procesar_lineas,
    procesar_preguntas_combinadas,
    leer_y_procesar_csv,
    obtener_respuesta
)

# Ruta al archivo CSV para los tests
CSV_PATH = os.path.join(os.path.dirname(__file__),
                        '..', 'trivia_questions.csv')


def test_leer_archivo_csv_generador():
    """Test para verificar que el archivo CSV se carga correctamente como generador."""
    generador = leer_archivo_csv_generador(CSV_PATH)
    assert hasattr(
        generador, '__iter__'), "La función debe devolver un generador"
    linea = next(generador)
    assert isinstance(linea, list), "Cada línea debe ser una lista"


def test_seleccionar_preguntas_aleatorias_generador():
    """Test para verificar la selección aleatoria de preguntas."""
    generador = leer_archivo_csv_generador(CSV_PATH)
    seleccionadas = seleccionar_preguntas_aleatorias_generador(
        generador, num_preguntas=3)
    assert len(
        seleccionadas) == 3, "Debe seleccionar el número correcto de preguntas"
    assert all(isinstance(p, list)
               for p in seleccionadas), "Cada pregunta debe ser una lista"


def test_procesar_lineas():
    """Test para verificar el procesamiento de líneas a diccionarios."""
    generador = leer_archivo_csv_generador(CSV_PATH)
    preguntas = procesar_lineas(generador)
    assert isinstance(preguntas, list), "La salida debe ser una lista"
    assert all(isinstance(p, dict)
               for p in preguntas), "Cada elemento debe ser un diccionario"
    assert 'pregunta' in preguntas[0], "El diccionario debe tener la clave 'pregunta'"


def test_procesar_preguntas_combinadas():
    """Test para verificar la combinación y procesamiento de preguntas."""
    generador = leer_archivo_csv_generador(CSV_PATH)
    seleccionadas = seleccionar_preguntas_aleatorias_generador(
        generador, num_preguntas=2)
    combinadas = procesar_preguntas_combinadas(seleccionadas)
    assert isinstance(combinadas, list), "La salida debe ser una lista"
    assert len(combinadas) == 2, "Debe procesar el número correcto de preguntas"


def test_leer_y_procesar_csv():
    """Test para verificar la función principal de lectura y procesamiento del CSV."""
    preguntas_procesadas = leer_y_procesar_csv(CSV_PATH)
    assert isinstance(preguntas_procesadas,
                      list), "La salida debe ser una lista"
    assert len(
        preguntas_procesadas) > 0, "La lista de preguntas no debe estar vacía"


def test_obtener_respuesta(monkeypatch):
    """Test para verificar la función de obtener respuesta del usuario."""
    pregunta = {
        'pregunta': '¿Cuál es la capital de Francia?',
        'opcion_1': 'Madrid',
        'opcion_2': 'París',
        'opcion_3': 'Roma',
        'respuesta_correcta': 'París'
    }

    # Simular la entrada del usuario
    monkeypatch.setattr('builtins.input', lambda _: '2')
    puntos = obtener_respuesta(pregunta)
    assert puntos == 10, "La respuesta debe ser correcta y otorgar 10 puntos"
