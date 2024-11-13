pipeline {
    agent any
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
        stage('Deploy Web App') {
            steps {
                echo "Desplegando aplicación web en EC2..."
                sh """
                # Actualiza pip
                ${PYTHON_VERSION} -m pip install --upgrade pip

                # Instala las dependencias
                ${PYTHON_VERSION} -m pip install -r ${PROJECT_DIR}/requirements.txt --user

                # Detiene cualquier instancia anterior de la aplicación
                pkill -f "uvicorn app:app" || true

                # Ejecuta la aplicación en segundo plano
                nohup ${PYTHON_VERSION} -m uvicorn app:app --host 0.0.0.0 --port 8000 &
                """
            }
        }
    }
    post {
        always {
            echo "Pipeline maestra finalizada."
        }
        failure {
            echo "La pipeline maestra falló."
        }
        success {
            echo "La pipeline maestra se ejecutó exitosamente."
        }
    }
}
