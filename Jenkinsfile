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
                echo "Generando documentación PyDoc..."
                sh """
                cd ${PROJECT_DIR}
                # Crear los archivos HTML de la documentación directamente en el directorio 'docs'
                mkdir -p ${DOCS_DIR}
                find . -name "*.py" ! -name "__init__.py" -exec python -m pydoc {} > ${DOCS_DIR}/{}.html \;
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
