pipeline {
    agent {
        node {
            label 'docker-agent-python'
        }
    }
    environment {
        PROJECT_DIR = 'src'
    }
    stages {
        stage('Checkout Código') {
            steps {
                echo "Obteniendo el código del repositorio..."
                checkout scm
            }
        }
        stage('Ejecutar trivia-pipeline') {
            steps {
                echo "Ejecutando el pipeline de pruebas..."
                build job: 'trivia-pipeline', wait: true  // Ejecuta el pipeline trivia-pipeline
            }
        }
    }
    post {
        success {
            echo "Pipeline ejecutado exitosamente."
        }
        failure {
            echo "El pipeline falló."
        }
    }
}
