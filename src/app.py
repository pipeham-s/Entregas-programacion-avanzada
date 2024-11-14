import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Directorio actual
current_dir = os.path.dirname(__file__)

# Rutas para los recursos estáticos
htmlcov_dir = os.path.join(current_dir, "Entregable_1", "htmlcov")
javadoc_dir = os.path.join(current_dir, "Entregable_2", "docs")

# Verificar existencia de directorios
if not os.path.exists(htmlcov_dir):
    raise RuntimeError(f"Directory '{htmlcov_dir}' does not exist")

if not os.path.exists(javadoc_dir):
    raise RuntimeError(f"Directory '{javadoc_dir}' does not exist")

# Montar los directorios como archivos estáticos
app.mount("/trivia/coverage", StaticFiles(directory=htmlcov_dir), name="coverage")
app.mount("/entregable2/javadoc",
          StaticFiles(directory=javadoc_dir), name="javadoc")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Proyecto Integrado</h1>
    <ul>
        <li><a href="/trivia">Módulo Trivia</a></li>
        <li><a href="/trivia/coverage">Reporte de Cobertura - Trivia</a></li>
        <li><a href="/entregable2/javadoc">Javadoc - Entregable 2</a></li>
        <li><a href="/pedidos">Módulo Pedidos</a></li>
    </ul>
    """


@app.get("/trivia", response_class=HTMLResponse)
def trivia():
    return "<h2>Módulo Trivia</h2><p>Esta es la aplicación del módulo de trivia.</p>"


@app.get("/trivia/coverage", include_in_schema=False)
async def redirect_to_coverage_index():
    return RedirectResponse(url="/trivia/coverage/index.html")

# Redirección a Javadoc


@app.get("/entregable2/javadoc", include_in_schema=False)
async def redirect_to_javadoc_index():
    return RedirectResponse(url="/entregable2/javadoc/index.html")

# Endpoint para el módulo de pedidos


@app.get("/pedidos", response_class=HTMLResponse)
def pedidos():
    return """
    <h2>Módulo Pedidos</h2>
    <p>Esta es la aplicación del módulo de pedidos.</p>
    <ul>
        <li><a href="/entregable2/javadoc">Ver Javadoc del módulo Pedidos</a></li>
    </ul>
    """


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
