pipeline {
    agent any
    stages {
        stage('build') {
     steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
             
                }
            }
                }
   
        }
    }
