// Jenkinsfile
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh 'pytest tests/'
                sh 'python validate_model.py'
            }
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker build -t mymodel:latest .'
                sh 'docker push myregistry/mymodel:latest'
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }
}
