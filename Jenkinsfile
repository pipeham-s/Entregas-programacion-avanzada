pipeline {
    agent any
    environment {
        PROJECT_DIR = 'src/Entregable_3'
        DOCS_DIR = 'src/Entregable_3/docs'
    }
    stages {
        stage('Build-Pedidos') {
            steps {
                echo "Compilando el proyecto de Python..."
                sh """
                cd ${PROJECT_DIR}
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }
        stage('PyDocs-Pedidos') {
            steps {
                echo "Generando documentación PyDoc del módulo pedidos..."
                sh """
                cd ${PROJECT_DIR}
                # Generar documentación con pydoc y guardarla en el directorio de docs
                find . -name "*.py" ! -name "__init__.py" -exec python -m pydoc -w {} \;
                mv *.html ${DOCS_DIR}
                """
            }
        }
    }
    post {
        always {
            echo "Pipeline finalizado."
        }
    }
}
