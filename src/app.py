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
usql_docs_dir = os.path.join(current_dir, "Entregable_3", "docs")

# Verificar existencia de directorios
if not os.path.exists(htmlcov_dir):
    raise RuntimeError(f"Directory '{htmlcov_dir}' does not exist")

if not os.path.exists(javadoc_dir):
    raise RuntimeError(f"Directory '{javadoc_dir}' does not exist")

if not os.path.exists(usql_docs_dir):
    raise RuntimeError(f"Directory '{usql_docs_dir}' does not exist")

# Montar los directorios como archivos estáticos
app.mount("/trivia/coverage", StaticFiles(directory=htmlcov_dir), name="coverage")
app.mount("/entregable2/javadoc",
          StaticFiles(directory=javadoc_dir), name="javadoc")
app.mount("/usql/pydoc", StaticFiles(directory=usql_docs_dir), name="pydoc")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Proyecto Integrado</h1>
    <ul>
        <li><a href="/trivia/coverage">Trivia - Reporte de Cobertura</a></li>
        <li><a href="/pedidos/javadoc">Pedidos - Javadoc</a></li>
        <li><a href="/usql/pydoc">USQL - Pydoc</a></li>
    </ul>
    """


@app.get("/trivia/coverage", include_in_schema=False)
async def redirect_to_coverage_index():
    return RedirectResponse(url="/trivia/coverage/index.html")


@app.get("/pedidos/javadoc", include_in_schema=False)
async def redirect_to_javadoc_index():
    return RedirectResponse(url="/entregable2/javadoc/index.html")


@app.get("/usql/pydoc", response_class=HTMLResponse)
def pydoc_usql():
    return """
    <h1>Documentación Pydoc - USQL</h1>
    <ul>
        <li><a href="/usql/pydoc/createDB.html">createDB</a></li>
        <li><a href="/usql/pydoc/lexer.html">lexer</a></li>
        <li><a href="/usql/pydoc/parser.html">parser</a></li>
        <li><a href="/usql/pydoc/primer_enfoque_dsl.html">primer_enfoque_dsl</a></li>
        <li><a href="/usql/pydoc/test_lexer.html">test_lexer</a></li>
        <li><a href="/usql/pydoc/test_parser.html">test_parser</a></li>
        <li><a href="/usql/pydoc/parsetab.html">parsetab</a></li>
    </ul>
    """


# Endpoint para el módulo de pedidos
@app.get("/pedidos", response_class=HTMLResponse)
def pedidos():
    return "<h2>Módulo Pedidos</h2><p>Esta es la aplicación del módulo de pedidos.</p>"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
