pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'bash jenkins/build-images.sh'
            }
	    }
        stage('Deploy') {
            steps {
                sh 'bash jenkins/deploy.sh'
            }
        }
    }
}