pipeline {
    agent any
    environment {
        PROJECT_DIR = 'src'
        PYTHON_VERSION = 'python3'
    }
    stages {
        stage('Checkout Código') {
            steps {
                echo "Obteniendo el código del repositorio..."
                checkout scm
            }
        }
        stage('Instalar Dependencias') {
            steps {
                echo "Instalando dependencias y configurando entorno virtual..."
                sh """
                    apt-get update -y
                    apt-get install -y ${PYTHON_VERSION}-venv
                    cd ${PROJECT_DIR}
                    ${PYTHON_VERSION} -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }
        stage('Desplegar Aplicación') {
            steps {
                echo "Desplegando la aplicación..."
                sh """
                    cd ${PROJECT_DIR}
                    . venv/bin/activate

                    # Detener cualquier instancia anterior de la aplicación
                    pkill -f "uvicorn app:app" || true

                    # Iniciar la aplicación en segundo plano
                    nohup venv/bin/python -m uvicorn app:app --host 0.0.0.0 --port 8000 > uvicorn.log 2>&1 &
                """
                echo "La aplicación web está corriendo en http://localhost:8000"
            }
        }
    }
    post {
        success {
            echo "Despliegue exitoso."
        }
        failure {
            echo "El despliegue falló."
        }
    }
}
