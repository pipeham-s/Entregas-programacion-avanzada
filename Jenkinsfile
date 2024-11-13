pipeline {
    agent any
    environment {
        IMAGE_NAME = 'mi-aplicacion-fastapi'
        CONTAINER_NAME = 'mi-contenedor-fastapi'
        DOCKER_HOST = 'unix:///var/run/docker.sock'
        DOCKER_TLS_VERIFY = '0'
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
                    docker build --network=host -t ${IMAGE_NAME} .
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
                    docker run -d --name ${CONTAINER_NAME} --network=host -p 8000:8000 ${IMAGE_NAME}
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
