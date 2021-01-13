pipeline{

    stages{
    
        stage('deploy'){
            sh 'python3 manage.py runserver 127.0.0.1:8081'
        }
        
        stage('test'){
            echo 'test'
        }
    
    }

}
