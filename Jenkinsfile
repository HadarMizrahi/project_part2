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
        stage ('Install ') {
            steps {
	        script {
                	sh 'python -m pip install --upgrade pip'
            	}
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
        stage('Run functions backend testing') {
            steps {
                bat 'python function_backend_testing.py'
            }
        }
        stage('Run backend testing') {
            steps {
                bat 'python backend_testing.py'
            }
        }
        stage('Run frontend testing') {
            steps {
                bat 'python frontend _testing.py'
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
