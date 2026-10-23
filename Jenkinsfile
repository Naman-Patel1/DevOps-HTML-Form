
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Check Required Files') {
            steps {
                bat 'if not exist index.html exit /b 1'
                bat 'if not exist test_form.py exit /b 1'
                echo 'HTML and test files found.'
            }
        }

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\jitin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version'
            }
        }

        stage('Run Automated Tests') {
            steps {
                bat '"C:\\Users\\jitin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m unittest -v test_form.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed.'
        }
        failure {
            echo 'FAILURE: Check the stage error in Console Output.'
        }
    }
}
