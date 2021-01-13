pipeline{

    agent any
    stages{
        stage('begin'){
            steps{
                echo 'begin'
            }
        }
    
        stage('deploy'){
            steps{
                sh 'python3 manage.py runserver 0.0.0.0:8081'
            }
            
        }
        
        stage('test'){
            steps{
                echo 'test'
            }
            
        }
    
    }

}
