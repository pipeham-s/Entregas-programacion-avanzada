pipeline {
    agent any
    environment {
        PROJECT_DIR = 'src/Entregable_1'
        PYTHON_VERSION = 'python3'
        VENV_DIR = 'venv'
    }
    stages {
        stage('Setup') {
            steps {
                echo "Instalando dependencias..."
                sh """
                cd ${PROJECT_DIR}
                if [ ! -d ${VENV_DIR} ]; then
                    ${PYTHON_VERSION} -m venv ${VENV_DIR}
                fi
                source ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }
        stage('Test') {
            steps {
                echo "Ejecutando tests..."
                sh """
                cd ${PROJECT_DIR}
                source ${VENV_DIR}/bin/activate
                ${PYTHON_VERSION} -m pytest --cov=trivia --cov-report=term --cov-report=html
                """
            }
        }
        stage('Report') {
            steps {
                echo "Generando reporte de cobertura..."
                publishHTML(target: [
                    reportDir: "${PROJECT_DIR}/htmlcov",
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
                source ${PROJECT_DIR}/${VENV_DIR}/bin/activate
                nohup python -m uvicorn app:app --host 0.0.0.0 --port 8000 &
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
