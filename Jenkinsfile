pipeline {
    agent any
    environment {
        IMAGE_NAME = 'mi-aplicacion-fastapi'
        CONTAINER_NAME = 'mi-contenedor-fastapi'
    }
    stages {
        stage('Checkout Código') {
            steps {
                echo "Obteniendo el código del repositorio..."
                checkout scm
            }
        }
        stage('Construir Imagen Docker de la Aplicación') {
            steps {
                echo "Construyendo la imagen Docker de la aplicación..."
                sh """
                    cd src
                    docker build -t ${IMAGE_NAME} .
                """
            }
        }
        stage('Desplegar Aplicación en Contenedor Docker') {
            steps {
                echo "Desplegando la aplicación en un contenedor Docker..."
                // Detener cualquier contenedor existente
                sh """
                    docker rm -f ${CONTAINER_NAME} || true
                """
                // Ejecutar el contenedor en segundo plano
                sh """
                    docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}
                """
            }
        }
    }
    post {
        success {
            echo "La aplicación web está corriendo en http://localhost:8000"
        }
        failure {
            echo "La pipeline falló. No se desplegará la aplicación web."
        }
    }
}
