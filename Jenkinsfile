pipeline{

    stages{
        stage('begin'){
            steps{
                echo 'begin'
            }
        }
    
        stage('deploy'){
            steps{
                sh 'python3 manage.py runserver 127.0.0.1:8081'
            }
            
        }
        
        stage('test'){
            steps{
                echo 'test'
            }
            
        }
    
    }

}
