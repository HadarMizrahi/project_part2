pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                }
            }
        }
        stage ('Github repository') {
            steps {
                git 'https://github.com/HadarMizrahi/project_part2.git'
            }
        }
        stage('Run backend server') {
            steps {
                bat 'start /min python rest_app.py'
            }
        }
        stage('Run frontend server') {
            steps {
                bat 'start /min python web_app.py'
            }
        }
        stage('Run backend testing') {
            steps {
                bat 'python backend_testing.py'
            }
        }
        stage('Run frontend testing') {
            steps {
                bat 'python frontend_testing.py'
            }
        }
        stage('Run combined testing') {
            steps {
                bat 'python combined_testing.py'
            }
        }
        stage('Run clean environment') {
            steps {
                bat 'python clean_environment.py'
            }
        }
    }
}
