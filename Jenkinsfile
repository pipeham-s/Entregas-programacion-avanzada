pipeline {
    agent {
        node {
            label 'docker-agent-python'
        }
    }
    environment {
        PROJECT_DIR = 'src'
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
                    python3 -m venv ${PROJECT_DIR}/venv
                    . ${PROJECT_DIR}/venv/bin/activate
                    pip install --upgrade pip
                    pip install -r ${PROJECT_DIR}/requirements.txt
                """
            }
        }
        stage('Desplegar Aplicación') {
            steps {
                echo "Desplegando la aplicación..."
                sh """
                    . ${PROJECT_DIR}/venv/bin/activate

                    # Detener cualquier instancia anterior de la aplicación
                    pkill -f "uvicorn app:app" || true

                    # Iniciar la aplicación en segundo plano
                    nohup python -m uvicorn app:app --host 0.0.0.0 --port 8000 > uvicorn.log 2>&1 &
                """
                echo "La aplicación web está corriendo en http://localhost:8000"
            }
        }
    }
    post {
        success {
            echo "Despliegue completado exitosamente."
        }
        failure {
            echo "El despliegue falló."
        }
    }
}
