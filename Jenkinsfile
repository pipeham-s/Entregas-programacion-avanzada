pipeline {
    agent any
    stages {
        stage('Run Trivia Pipeline') {
            steps {
                build job: 'trivia-pipeline'
            }
        }
        stage('Deploy FastAPI App') {
            steps {
                echo "Desplegando FastAPI..."
                sh """
                cd src
                source Entregable_1/venv/bin/activate
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
