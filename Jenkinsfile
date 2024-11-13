pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root:root'
        }
    }
    environment {
        PROJECT_DIR = 'src'
        PYTHON_VERSION = 'python3'
    }
    stages {
        stage('Build Entregable_1') {
            steps {
                echo "Ejecutando pipeline de Entregable_1..."
                build job: 'trivia-pipeline', wait: true
            }
        }
        stage('Setup Python Environment') {
            steps {
                echo "Instalando python3-venv y configurando entorno virtual..."
                sh """
                    apt update -y && apt install -y ${PYTHON_VERSION}-venv

                    # Navegar al directorio del proyecto
                    cd ${PROJECT_DIR}

                    # Crear entorno virtual
                    ${PYTHON_VERSION} -m venv venv

                    # Activar entorno virtual
                    . venv/bin/activate

                    # Actualizar pip en el entorno virtual
                    pip install --upgrade pip

                    # Instalar dependencias en el entorno virtual
                    pip install -r requirements.txt
                """
            }
        }
        stage('Deploy Web App') {
            steps {
                echo "Desplegando aplicación web..."
                sh """
                    cd ${PROJECT_DIR}

                    # Activar entorno virtual
                    . venv/bin/activate

                    # Detener cualquier instancia anterior de la aplicación
                    pkill -f "uvicorn app:app" || true

                    # Ejecutar la aplicación en segundo plano
                    nohup venv/bin/python -m uvicorn app:app --host 0.0.0.0 --port 8000 &
                """
            }
        }
    }
    post {
        always {
            echo "Pipeline maestra finalizada."
            cleanWs()
        }
        failure {
            echo "La pipeline maestra falló."
        }
        success {
            echo "La pipeline maestra se ejecutó exitosamente."
        }
    }
}
