pipeline {
    agent any

    tools {
        jdk 'jdk17'
    }

    environment {
        SONAR_SCANNER_HOME = tool name: 'SonarScanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/iamdeepaktiwari08/jenkins-sonarqube-cicd.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh """
                    ${SONAR_SCANNER_HOME}/bin/sonar-scanner
                    """
                }
            }
        }
    }
}