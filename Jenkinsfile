pipeline {
    agent {
        node {
            label 'docker-agent-python'
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
                    cd ${PROJECT_DIR}
                    ${PYTHON_VERSION} -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }
        stage('Run Tests') {
            steps {
                echo "Ejecutando pruebas unitarias..."
                sh """
                    cd ${PROJECT_DIR}
                    . venv/bin/activate
                    pytest
                """
            }
        }
    }
    post {
        success {
            echo "Pipeline ejecutada exitosamente. Iniciando el despliegue de la web..."
            sh """
                cd ${PROJECT_DIR}
                . venv/bin/activate

                # Detener cualquier instancia anterior de la aplicación
                pkill -f "uvicorn app:app" || true

                # Iniciar la aplicación web en segundo plano
                nohup venv/bin/python -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload > uvicorn.log 2>&1 &
            """
            echo "La aplicación web está corriendo en http://localhost:8000"
        }
        failure {
            echo "La pipeline falló. No se desplegará la aplicación web."
        }
        always {
            echo "Limpieza del workspace."
            deleteDir()
        }
    }
}
