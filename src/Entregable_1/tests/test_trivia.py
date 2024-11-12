import pytest
import os
from trivia import (
    leer_archivo_csv_generador,
    seleccionar_preguntas_aleatorias_generador,
    procesar_lineas,
    procesar_preguntas_combinadas,
    leer_y_procesar_csv,
    obtener_respuesta,
    generar_documentacion,
    validate_input,
    obtener_respuesta,
    mostrar_bienvenida,
    jugar,
    jugar_recursivo,
    obtener_respuesta,
    leer_y_procesar_csv
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


def test_generar_documentacion(capsys):
    """Test para verificar que la documentación se genera correctamente."""
    generar_documentacion()
    captured = capsys.readouterr()  # Captura la salida de la consola
    assert "Función:" in captured.out, "No se generó la documentación correctamente"
    assert "Descripción:" in captured.out, "No se mostraron las descripciones de las funciones"


@validate_input
def funcion_de_prueba(num):
    """Función de prueba para el decorador validate_input."""
    return int(num)


def test_validate_input_con_valor_invalido(capsys):
    """Test para verificar que el decorador maneja correctamente ValueError."""
    resultado = funcion_de_prueba("texto")  # Esto debería causar un ValueError
    captured = capsys.readouterr()
    assert "Por favor ingresa solo números." in captured.out, "El mensaje de error no se mostró correctamente"
    assert resultado is None, "La función debería devolver None cuando ocurre un ValueError"


def test_obtener_respuesta_con_respuesta_invalida(monkeypatch, capsys):
    """Test para verificar que se maneja correctamente una respuesta inválida del usuario."""
    pregunta = {
        'pregunta': '¿Cuál es la capital de Francia?',
        'opcion_1': 'Madrid',
        'opcion_2': 'París',
        'opcion_3': 'Roma',
        'respuesta_correcta': 'París'
    }

    # Simular una respuesta inválida del usuario
    # Primero una respuesta inválida ('4'), luego una válida ('2')
    respuestas = iter(['4', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(respuestas))

    obtener_respuesta(pregunta)
    captured = capsys.readouterr()
    assert "Respuesta inválida. Inténtalo de nuevo." in captured.out, "El mensaje de respuesta inválida no se mostró correctamente"


def test_mostrar_bienvenida(monkeypatch, capsys):
    """Test para verificar que la función mostrar_bienvenida se ejecuta correctamente."""
    monkeypatch.setattr(
        'builtins.input', lambda: None)  # Simula que el usuario presiona ENTER
    mostrar_bienvenida()
    captured = capsys.readouterr()
    assert "¡Bienvenido al Trivial!" in captured.out, "El mensaje de bienvenida no se mostró correctamente"


def test_jugar_recursivo(monkeypatch):
    """Test para verificar la función jugar_recursivo con respuestas simuladas."""
    preguntas = [
        {'pregunta': '¿Cuál es la capital de Francia?', 'opcion_1': 'Madrid',
            'opcion_2': 'París', 'opcion_3': 'Roma', 'respuesta_correcta': 'París'},
        {'pregunta': '¿Cuál es 2+2?', 'opcion_1': '3', 'opcion_2': '4',
            'opcion_3': '5', 'respuesta_correcta': '4'}
    ]

    # Simular respuestas del usuario
    respuestas = iter(['2', '2'])  # Ambas respuestas son correctas
    monkeypatch.setattr('builtins.input', lambda _: next(respuestas))

    total_puntos = jugar_recursivo(preguntas, resultados=[])
    assert total_puntos == 20, "La puntuación final debería ser 20 puntos"


def test_jugar(monkeypatch):
    """Test para verificar la función jugar con respuestas simuladas."""
    # Simular respuestas del usuario (todas correctas) y luego no volver a jugar
    # Proporcionamos suficientes respuestas para evitar StopIteration
    # Agregamos más respuestas para cubrir todas las preguntas
    respuestas = iter(['2', '2', '2', '2', '2', 'n'])
    monkeypatch.setattr('builtins.input', lambda _: next(respuestas))

    # Ejecutar la función jugar y validar que no hay errores
    try:
        jugar()
    except StopIteration:
        pytest.fail(
            "El test falló debido a StopIteration. No se proporcionaron suficientes respuestas.")
