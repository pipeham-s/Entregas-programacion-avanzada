from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Determinar el directorio actual
current_dir = os.path.dirname(__file__)

# Montar el directorio 'htmlcov' como archivos estáticos bajo '/trivia/coverage'
htmlcov_dir = os.path.join(current_dir, "Entregable_1", "htmlcov")
app.mount("/trivia/coverage", StaticFiles(directory=htmlcov_dir), name="coverage")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Proyecto Integrado</h1>
    <ul>
        <li><a href="/trivia">Módulo Trivia</a></li>
        <li><a href="/trivia/coverage">Reporte de Cobertura - Trivia</a></li>
        </ul>
    """


@app.get("/trivia", response_class=HTMLResponse)
def trivia():
    return "<h2>Módulo Trivia</h2><p>Esta es la aplicación del módulo de trivia.</p>"

# Redirigir '/trivia/coverage' a '/trivia/coverage/index.html'


@app.get("/trivia/coverage", include_in_schema=False)
async def redirect_to_coverage_index():
    return RedirectResponse(url="/trivia/coverage/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
