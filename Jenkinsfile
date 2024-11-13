pipeline {
    agent {
        node {
            label 'docker-agent'
        }
    }
    environment {
        IMAGE_NAME = 'mi-aplicacion-fastapi'
        CONTAINER_NAME = 'mi-contenedor-fastapi'
    }
    stages {
        stage('Verificar Docker') {
            steps {
                echo "Verificando acceso al daemon Docker..."
                sh 'docker version || exit 1'
            }
        }
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
                    docker build -t ${IMAGE_NAME} --network=host .
                """
            }
        }
        stage('Desplegar Aplicación en Contenedor Docker') {
            steps {
                echo "Desplegando la aplicación en un contenedor Docker..."
                sh """
                    docker rm -f ${CONTAINER_NAME} || true
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
