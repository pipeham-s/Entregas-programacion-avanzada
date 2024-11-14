pipeline {
    agent any
    environment {
        PROJECT_DIR = 'src/Entregable_1'
        PYTHON_VERSION = 'python3'
        VENV_DIR = '/var/lib/jenkins/venv'  // Ruta fija para el entorno virtual
    }
    stages {
        stage('Setup') {
            steps {
                echo "Instalando dependencias globales..."
                sh """
                #!/bin/bash
                if [ ! -d ${VENV_DIR} ]; then
                    ${PYTHON_VERSION} -m venv ${VENV_DIR}
                fi
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r ${PROJECT_DIR}/requirements.txt
                """
            }
        }
        stage('Test') {
            steps {
                echo "Ejecutando tests..."
                sh """
                #!/bin/bash
                cd ${PROJECT_DIR}
                . ${VENV_DIR}/bin/activate
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
                #!/bin/bash
                cd src
                . ${VENV_DIR}/bin/activate
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
