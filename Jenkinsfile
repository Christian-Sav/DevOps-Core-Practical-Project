pipeline {
    agent any
    stages {
        stage('Run unit tests') {
            steps {
                sh "bash test.sh"
            }
        }
        stage('build and push') {
            environment {
                DOCKER_CREDS = credentials('docker_creds')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u ${DOCKER_CREDS_USR} -p ${DOCKER_CREDS_PSW}"
                sh "docker-compose push"
                sh "/bin/bash -c 'docker rmi \$(docker images -q)'"
            }
        }
        stage('deploy stack') {
            steps {
                sh "scp ./docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml"
                sh "scp ./nginx.conf jenkins@swarm-manager:/home/jenkins/nginx.conf"
                sh "ssh jenkins@swarm-manager < deploy.sh"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: "*/htmlcov/*"
        }
    } 
}