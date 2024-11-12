from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from Entregable_1.trivia import leer_y_procesar_csv

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Proyecto Integrado</h1>
    <ul>
        <li><a href="/trivia">Módulo Trivia</a></li>
        <li><a href="/pedidos">Módulo Sistema de Pedidos (Próximamente)</a></li>
        <li><a href="/usql">Módulo Procesador de Consultas USQL (Próximamente)</a></li>
    </ul>
    """


@app.get("/trivia", response_class=HTMLResponse)
def trivia():
    preguntas = leer_y_procesar_csv('Entregable_1/trivia_questions.csv')
    return f"<h2>Módulo Trivia</h2><p>Preguntas procesadas: {len(preguntas)}</p>"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
