# Utiliza una imagen base ligera de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos e instálalos
COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY src/ /app/

# Expone el puerto en el que se ejecutará Uvicorn
EXPOSE 8000

# Comando para iniciar la aplicación FastAPI con Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
