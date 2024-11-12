pipeline {
    agent any
    stages {
        stage('Build Entregable_1') {
            steps {
                echo "Ejecutando pipeline de Entregable_1..."
                // Llama al job 'trivia-pipeline' y espera a que termine
                build job: 'trivia-pipeline', wait: true
            }
        }
        stage('Deploy Web App') {
            steps {
                echo "Desplegando aplicación web en EC2..."
                sh """
                # Cambia al directorio src
                cd src
                # Instala las dependencias
                pip3 install -r requirements.txt --user
                # Mata cualquier instancia anterior de la aplicación
                pkill -f "uvicorn app:app" || true
                # Ejecuta la aplicación en segundo plano
                nohup python3 -m uvicorn app:app --host 0.0.0.0 --port 8000 &
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
