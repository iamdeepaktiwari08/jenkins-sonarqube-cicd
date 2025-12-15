pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/iamdeepaktiwari08/jenkins-sonarqube-cicd.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {   // 🔴 MUST MATCH SYSTEM NAME
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=jenkins-sonarqube-cicd \
                    -Dsonar.projectName=jenkins-sonarqube-cicd \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://3.80.65.95:9000
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}