pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                echo 'Code cloned from GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }

        stage('Deploy Application') {
            steps {
                sh 'nohup python3 app.py > output.log 2>&1 &'
            }
        }
    }
}
