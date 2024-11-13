pipeline {
    agent any
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
        # Define variables de entorno si es necesario
        PROJECT_DIR="src"
        PYTHON_VERSION="python3"

        cd ${PROJECT_DIR}

        # Crear entorno virtual
        ${PYTHON_VERSION} -m venv venv

        # Activar entorno virtual
        source venv/bin/activate

        # Actualizar pip en el entorno virtual
        pip install --upgrade pip

        # Instalar dependencias en el entorno virtual
        pip install -r requirements.txt

        # Detener cualquier instancia anterior de la aplicación
        pkill -f "uvicorn app:app" || true

        # Ejecutar la aplicación en segundo plano usando el entorno virtual
        nohup venv/bin/python -m uvicorn app:app --host 0.0.0.0 --port 8000 &
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
