pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh touch test.txt
                sh ls -a
                // Add your build commands here.
            }
        }

        stage('Deploy') {
            steps {
                echo 'Testing...'
                // Add your test commands here.
            }
        }
    }

    post {
        always {
            echo 'Output'
        }
        success {
            echo 'Job succeeded!'
        }
        failure {
            echo 'Job failed!'
        }
    }
}
