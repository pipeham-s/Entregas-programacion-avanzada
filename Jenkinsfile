pipeline {
    agent any
    environment {
        PYTHON_VERSION = 'python3'
        VENV_DIR = '/var/lib/jenkins/venv'
        REQUIREMENTS_FILE = 'requirements.txt'
    }
    stages {
        stage('Setup') {
            steps {
                echo "Instalando dependencias globales..."
                sh """
                if [ ! -d ${VENV_DIR} ]; then
                    ${PYTHON_VERSION} -m venv ${VENV_DIR}
                fi
                bash -c "source ${VENV_DIR}/bin/activate && pip install --upgrade pip && pip install -r ${REQUIREMENTS_FILE}"
                """
            }
        }
        stage('Test') {
            steps {
                echo "Ejecutando tests..."
                sh """
                bash -c "source ${VENV_DIR}/bin/activate && ${PYTHON_VERSION} -m pytest --cov=trivia --cov-report=term --cov-report=html"
                """
            }
        }
        stage('Report') {
            steps {
                echo "Generando reporte de cobertura..."
                publishHTML(target: [
                    reportDir: "src/Entregable_1/htmlcov",
                    reportFiles: 'index.html',
                    reportName: 'Cobertura de Tests'
                ])
            }
        }
        stage('Deploy') {
            steps {
                echo "Desplegando FastAPI..."
                sh """
                cd src
                bash -c "source ${VENV_DIR}/bin/activate && nohup python -m uvicorn app:app --host 0.0.0.0 --port 8000 &"
                """
            }
        }
    }
    post {
        always {
            echo "Pipeline finalizado."
        }
        failure {
            echo "Pipeline falló. Verifica los errores."
        }
        success {
            echo "Pipeline ejecutado exitosamente."
        }
    }
}
