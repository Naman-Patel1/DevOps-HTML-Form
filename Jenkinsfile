
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Files') {
            steps {
                bat 'if not exist index.html exit /b 1'
                bat 'if not exist test_form.py exit /b 1'
                echo 'Required files found.'
            }
        }

        stage('Automated Tests') {
            steps {
                bat 'python -m unittest -v test_form.py'
            }
        }
    }

    post {
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Tests failed. Check Console Output.'
        }
    }
}
