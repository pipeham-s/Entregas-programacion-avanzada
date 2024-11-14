pipeline {
    agent any
    stages {
        stage('Build-Pedidos') {
            steps {
                echo "Compilando el proyecto de Python..."
                sh """
                cd /var/lib/jenkins/workspace/usql-pipeline/src/Entregable_3
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
                cd /var/lib/jenkins/workspace/usql-pipeline/src/Entregable_3
                # Crear los archivos HTML de la documentación directamente en el directorio 'docs'
                mkdir -p /var/lib/jenkins/workspace/usql-pipeline/src/Entregable_3/docs
                find . -name "*.py" ! -name "__init__.py" -exec python -m pydoc {} \\; -exec sh -c 'mv {} /var/lib/jenkins/workspace/usql-pipeline/src/Entregable_3/docs/$(basename {} .py).html' \\;
                """
            }
        }
    }
}
