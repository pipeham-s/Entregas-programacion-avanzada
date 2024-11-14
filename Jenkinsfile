pipeline {
    agent any
    environment {
        PROJECT_DIR = 'src/Entregable_1'  // Manteniendo la variable original
        PYTHON_VERSION = 'python3'
        VENV_DIR = '/var/lib/jenkins/venv'
        REQUIREMENTS_FILE = "${PROJECT_DIR}/requirements.txt"
    }
    stages {
        stage('Setup-Trivia') {
            steps {
                echo "Instalando dependencias globales..."
                sh """
                if [ ! -d ${VENV_DIR} ]; then
                    ${PYTHON_VERSION} -m venv ${VENV_DIR}
                fi
                bash -c "source ${VENV_DIR}/bin/activate && pip install --upgrade pip && pip install -r requirements.txt"
                """
            }
        }
        
        stage('Test-Trivia') {
            steps {
                echo "Ejecutando tests..."
                sh """
                cd ${PROJECT_DIR}
                bash -c "source ${VENV_DIR}/bin/activate && ${PYTHON_VERSION} -m pytest --cov=trivia --cov-report=term --cov-report=html"
                """
            }
        }
        
        stage('Report-Trivia') {
            steps {
                echo "Generando reporte de cobertura..."
                publishHTML(target: [
                    reportDir: "${PROJECT_DIR}/htmlcov",
                    reportFiles: 'index.html',
                    reportName: 'Cobertura de Tests'
                ])
            }
        }

        // Integración del pipeline de pedidos
        stage('Build-Pedidos') {
            steps {
                echo "Compilando el proyecto de pedidos..."
                sh """
                cd src/Entregable_2/Code
                javac -d out \$(find . -name "*.java")
                """
            }
        }

        stage('Javadoc-Pedidos') {
            steps {
                echo "Generando Javadoc del módulo pedidos..."
                sh """
                bash -c "javadoc -d src/Entregable_2/docs -sourcepath src -subpackages Entregable_2.Code"
                """
            }
        }

        stage('Build-Usql') {
            steps {
                echo "Compilando el proyecto de Python..."
                sh """
                cd src/Entregable_3
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }
  stage('PyDocs-Usql') {
    steps {
        echo "Generando documentación PyDoc..."
        sh """
        bash -c '
        cd src/Entregable_3
        . venv/bin/activate
        mkdir -p docs
        for file in \$(find . -path "./venv" -prune -o -name "*.py" ! -name "__init__.py" -print); do
            python -m pydoc -w \$file || echo "Error al generar documentación para \$file"
            mv \$(basename \${file} .py).html docs/ || echo "Archivo HTML no encontrado para \$file"
        done
        '
        """
    }
}

        // Despliegue del servicio Uvicorn
        stage('Deploy') {
            steps {
                echo "Iniciando servicio Uvicorn..."
                sh "sudo systemctl restart uvicorn"
            }
        }
    }
    post {
    always {
        echo "Pipeline finalizado."
        mail to: 'tu_correo@dominio.com',
             subject: "Jenkins Pipeline: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
             body: "El pipeline ${env.JOB_NAME} ha finalizado con estado: ${currentBuild.currentResult}\nRevisa los detalles en: ${env.BUILD_URL}"
    }
    failure {
        echo "Pipeline falló. Verifica los errores."
    }
    success {
        echo "Pipeline ejecutado exitosamente."
    }
}


}
